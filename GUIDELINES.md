# Workshop guidelines

Design principles for this RAG-and-evals workshop, distilled from review
feedback. These are the rules the codebase should keep following.

## 1. One RAG stack — don't compare algorithms

Use a **single retrieval stack everywhere**:

- **Embedding model:** OpenAI `text-embedding-3-small`
- **Vector store:** ChromaDB (persistent, cosine)
- **Answer step:** Claude (`claude-opus-4-8`), grounded strictly in retrieved context

Do **not** reintroduce lexical/TF-IDF or alternate retrievers as "versions."
The model and the store stay fixed so experiments are attributable.

## 2. The only experiment knobs are chunk size and K

Hold the **model** and the **eval set** fixed; vary exactly one of:

- **chunk size** — `chunking/` (how a record becomes the indexed text)
- **K** — a run-time flag

Then read the effect on **Recall / Precision / MRR**. Changing model *and*
questions at once makes results uninterpretable — never do it.

## 3. One shared eval set: `corpora/ruler.jsonl`

All questions for **coins and rolex live in one file**, one JSON object per
line. No per-version and no per-corpus eval files. Fields:

| field | meaning |
|---|---|
| `corpus` | `coins` \| `rolex` (filtered by `--corpus`; `both` uses all) |
| `id` | stable question id |
| `question` | the query |
| `type` | one unified taxonomy (below) |
| `relevant` | correct doc id(s) → grades retrieval |
| `answer` | the correct answer → the LLM judge grades against it (omit for pure-retrieval Qs) |

**One taxonomy** for every question, coins and rolex alike:
`direct_lookup · buried_detail · multi_hop · synthesis · out_of_corpus`.
Do not let corpus-specific categories (`shorthand`, `nickname`, …) creep back.

**One answer field.** Do not carry both a substring check and a reference.
The single `answer` field is the ground truth; the LLM judge grades against it.

## 4. Recall first, precision second

For a RAG, retrieved docs *are* the model's context, so **answer quality is
capped by retrieval**:

- Optimize **Recall@k** at a K the context window can afford — the needed doc
  must be in the top-K or the answer can't be right.
- Use **precision** as the cost/noise budget (context size, tokens,
  distraction) once recall is adequate.
- Use **MRR** as the tiebreaker — keep the best doc near the top.
- Prefer better chunking / reranking over simply cranking K.

## 5. Probes are a smoke test, not a metric

`probes` = one question per `type` (derived from the ruler). Use it to *eyeball*
that retrieval is sane after a change (`harness.ask --probes`). Use the full
ruler for actual numbers (`harness.sweep`, `harness.run`, `harness.label`).

## 6. Corpus and chunking are separate concerns

- `corpora/` owns **what we know** — source records + web-verified facts +
  ground truth. Facts must be real and sourced; never fabricate figures.
- `chunking/` owns **how a record becomes the indexed document**.

Keep them in separate folders so a data change and a chunking change never mix.

## 7. Use structured fields for superlative/aggregation queries

Vector search answers "find docs about X," not "compute the min/max over all
docs." For "rarest / highest mintage / most …" questions, sort/filter on the
structured field (e.g. `mintage`) via Chroma metadata — don't expect semantic
retrieval to get them right.

## 8. Operational

- Run everything from the **virtualenv** (`.venv`), where `openai`,
  `chromadb`, `anthropic` are installed — system `python3` will `ModuleNotFound`.
- Embeddings are **batched and cached** (`.embed_cache/`); the vector store
  persists (`.chroma/`). First build is the only slow step.
- **Never commit API keys** or paste them into shared channels; keep them in
  the shell env. The UI/tools degrade gracefully when a key is missing.

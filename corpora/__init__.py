"""Corpora for the workshop.

A *corpus* is a set of documents plus its ground-truth eval set. The harness
and every version's Rag are corpus-agnostic — they operate on generic
`Document` objects (id + prose text + structured meta), so the exact same
retrieval/eval code runs against coins OR Rolex watches. Swap corpora with
`--corpus` on the harness.
"""

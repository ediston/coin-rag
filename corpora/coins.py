"""The coins corpus: source records + verified facts.

This module is the CORPUS. It loads the raw CSV into structured records and
attaches web-verified fact sentences (from coins_facts.py). It does NOT build
the final document text — that formatting is the chunking layer's job
(chunking/coins.py), so we keep "what we know" separate from "how we present
it to the index".

A record is a plain dict:
  {
    "id":   "UK-1P-2020",
    "meta": {denomination, year, section, remarks, rarity, mintage, ...},
    "facts": ["verified sentence", ...],   # extra, corpus-provided prose
    "prose_only": bool,                     # if True, `facts` IS the whole doc
  }
"""

from __future__ import annotations

from corpora.coins_facts import EXTRA_DOCS, NOTABLE_FACTS, OVERVIEW
from harness.dataset import load_coins


def load_records() -> list[dict]:
    records: list[dict] = []

    if OVERVIEW:
        records.append({"id": "UK-OVERVIEW", "meta": {"kind": "overview"},
                        "facts": list(OVERVIEW), "prose_only": True})

    for c in load_coins():
        records.append({
            "id": c.ref,
            "meta": {
                "denomination": c.denomination,
                "year": c.year,
                "section": c.section,
                "remarks": c.remarks,
                "rarity": c.rarity_label,
                "mintage": c.mintage,
                "market_value": c.market_value,
            },
            "facts": list(NOTABLE_FACTS.get(c.ref, [])),
            "prose_only": False,
        })

    # Famous real coins that aren't CSV rows (e.g. the undated 20p mule) come
    # pre-written as prose.
    for e in EXTRA_DOCS:
        records.append({"id": e["id"], "meta": e.get("meta", {}),
                        "facts": [e["text"]], "prose_only": True})

    return records


if __name__ == "__main__":
    recs = load_records()
    print(f"{len(recs)} coin records")
    print(recs[1]["id"], recs[1]["meta"], recs[1]["facts"][:1])

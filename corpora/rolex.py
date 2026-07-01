"""The Rolex corpus: source records + verified facts.

Loads the web-verified reference data from rolex_data.json into structured
records. Like the coins corpus, it does NOT assemble the document text — that
is the chunking layer's job (chunking/rolex.py).
"""

from __future__ import annotations

import json
import os

DATA = os.path.join(os.path.dirname(__file__), "rolex_data.json")


def load_records() -> list[dict]:
    with open(DATA, encoding="utf-8") as f:
        rows = json.load(f)
    records = []
    for r in rows:
        records.append({
            "id": r["id"],
            "meta": {
                "model": r["model"],
                "reference": r["reference"],
                "nickname": r["nickname"],
                "production_years": r["production_years"],
            },
            "facts": list(r["specs"]),
            "prose_only": False,
        })
    return records


if __name__ == "__main__":
    recs = load_records()
    print(f"{len(recs)} Rolex records")
    print(recs[5]["id"], recs[5]["meta"])

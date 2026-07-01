"""The one document type every corpus produces and every version consumes."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Document:
    id: str                 # the unique doc id we retrieve, e.g. "UK-1P-2020"
    text: str               # the PROSE document a retriever indexes
    meta: dict = field(default_factory=dict)  # structured fields (fielded index / answer context)

    def meta_text(self) -> str:
        """All meta values flattened to a string — handy for context/answers."""
        return " | ".join(f"{k}: {v}" for k, v in self.meta.items() if v)

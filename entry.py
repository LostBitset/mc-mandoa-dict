from dataclasses import dataclass
import typing as t

@dataclass
class Word:
    text: str
    phon: str

@dataclass
class RawEntry:
    words: t.Dict[str, Word]

@dataclass
class Entry:
    pos: str
    words: RawEntry
    examples: t.List[RawEntry]


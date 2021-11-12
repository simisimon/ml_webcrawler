from dataclasses import dataclass
from typing import List

@dataclass
class Module:
    name: str
    href: str

@dataclass
class SciKitLearnModule:
    name: str
    modules: List




from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional, List, Dict

from models.card import Card

@dataclass_json
@dataclass
class ListData:
    id: str
    name: Optional[str] = None
    closed: bool = False
    pos: int = 0
    softLimit: Optional[str] = None
    idBoard: Optional[str] = None
    subscribed: bool = False
    limits: Optional[Dict] = None
    cards: Optional[List[Card]] = None

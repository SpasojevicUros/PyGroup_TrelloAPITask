from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional, List, Dict

@dataclass_json
@dataclass
class CheckItem:
    id: str
    name: str = ""
    nameData: Dict = field(default_factory=dict)
    pos: int = 0
    state: str = 'incomplete'
    due: Optional[str] = None
    dueReminder: Optional[str] = None
    idMember: Optional[str] = None
    idChecklist: Optional[str] = None

@dataclass_json
@dataclass
class CheckList:
    id: str
    name: str
    idBoard: str
    idCard: str
    pos: int = 0
    checkItems: List[CheckItem] = field(default_factory=list)

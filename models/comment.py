from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional, List, Dict

@dataclass_json
@dataclass
class Comment:
    id: str
    idMemberCreator: str = ''
    data: Dict = field(default_factory=dict)
    type: str = 'commentCard'
    date: Optional[str] = None

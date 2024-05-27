from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional, List, Dict

from models.list import ListData

@dataclass_json
@dataclass
class LabelNames:
    green: str = ""
    yellow: str = ""
    orange: str = ""
    red: str = ""
    purple: str = ""
    blue: str = ""
    sky: str = ""
    lime: str = ""
    pink: str = ""
    black: str = ""

@dataclass_json
@dataclass
class Board:
    id: str
    name: str
    desc: Optional[str] = None
    descData: Optional[Dict] = None
    closed: bool = False
    idMemberCreator: Optional[str] = None
    idOrganization: Optional[str] = None
    pinned: bool = False
    url: Optional[str] = None
    shortUrl: Optional[str] = None
    prefs: Optional[Dict] = None
    labelNames: Optional[LabelNames] = None
    starred: bool = False
    limits: Optional[Dict] = None
    memberships: Optional[str] = None
    enterpriseOwned: bool = False
    lists: Optional[List[ListData]] = None

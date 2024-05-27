from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional, List, Dict

from models.checklist import CheckList
from models.comment import Comment

@dataclass_json
@dataclass
class Label:
    id: str
    idBoard: str
    name: str
    color: str
    uses: int

@dataclass_json
@dataclass
class Card:
    id: str
    badges: Dict = field(default_factory=dict)
    checkItemStates: List[str] = field(default_factory=list)
    closed: bool = False
    dueComplete: bool = False
    dateLastActivity: Optional[str] = None
    desc: str = ''
    descData: Optional[Dict] = None
    due: Optional[str] = None
    dueReminder: Optional[str] = None
    email: Optional[str] = None
    idBoard: Optional[str] = None
    idChecklists: List[str] = field(default_factory=list)
    idList: Optional[str] = None
    idMembers: List[str] = field(default_factory=list)
    idMembersVoted: List[str] = field(default_factory=list)
    idShort: Optional[int] = None
    idAttachmentCover: Optional[str] = None
    labels: List[Label] = field(default_factory=list)
    idLabels: List[str] = field(default_factory=list)
    manualCoverAttachment: bool = False
    name: str = ""
    pos: int = 0
    shortLink: Optional[str] = None
    shortUrl: Optional[str] = None
    start: Optional[str] = None
    subscribed: bool = False
    url: Optional[str] = None
    cover: Optional[Dict] = None
    isTemplate: bool = False
    cardRole: Optional[str] = None
    checkLists: List[CheckList] = field(default_factory=list)
    comments: List[Comment] = field(default_factory=list)

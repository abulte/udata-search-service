import dataclasses
from typing import List
from datetime import date
from dateutil.parser import isoparse


@dataclasses.dataclass
class EntityBase():

    @classmethod
    def load_from_dict(cls, data):
        fields = [f.name for f in dataclasses.fields(cls)]
        data = {key: data[key] for key in data if key in fields}
        return cls(**data)

    def to_dict(self):
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Organization(EntityBase):
    id: str
    name: str
    description: str
    url: str
    orga_sp: int
    created_at: date
    followers: int
    datasets: int
    views: int
    reuses: int

    badges: List[str] | None = None
    acronym: str | None = None

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at = isoparse(self.created_at)


@dataclasses.dataclass
class Dataset(EntityBase):
    id: str
    title: str
    url: str
    created_at: date
    frequency: str
    format: List[str]
    views: int
    followers: int
    reuses: int
    featured: int
    resources_count: int
    concat_title_org: str
    description: str

    last_update: date | None = None
    acronym: str | None = None
    badges: List[str] | None = None
    tags: List[str] | None = None
    license: str | None = None
    temporal_coverage_start: date | None = None
    temporal_coverage_end: date | None = None
    granularity: str | None = None
    geozones: List[str] | None = None
    schema: List[str] | None = None
    topics: List[str] | None = None

    orga_sp: int | None = None
    orga_followers: int | None = None
    organization: str | None = None
    organization_name: str | None = None
    organization_badges: List[str] | None = None
    owner: str | None = None

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at = isoparse(self.created_at)
        if isinstance(self.last_update, str):
            self.last_update = isoparse(self.last_update)
        if isinstance(self.temporal_coverage_start, str):
            self.temporal_coverage_start = isoparse(self.temporal_coverage_start)
        if isinstance(self.temporal_coverage_end, str):
            self.temporal_coverage_end = isoparse(self.temporal_coverage_end)


@dataclasses.dataclass
class Reuse(EntityBase):
    id: str
    title: str
    url: str
    created_at: date
    views: int
    followers: int
    datasets: int
    featured: int
    description: str
    type: str
    topic: str

    tags: List[str] | None = None
    badges: List[str] | None = None
    orga_followers: int | None = None
    organization: str | None = None
    organization_name: str | None = None
    organization_badges: List[str] | None = None
    owner: str | None = None

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at = isoparse(self.created_at)


@dataclasses.dataclass
class Dataservice(EntityBase):
    id: str
    title: str
    description: str
    description_length: float
    created_at: date

    views: int = 0
    followers: int = 0
    is_restricted: bool | None = None
    orga_followers: int | None = None
    organization: str | None = None
    organization_name: str | None = None
    owner: str | None = None
    tags: List[str] | None = None

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at = isoparse(self.created_at)

@dataclasses.dataclass
class Topic(EntityBase):
    id: str
    name: str
    created_at: date
    featured: bool
    featured_score: int

    description: str | None = None
    owner: str | None = None
    tags: List[str] | None = None
    granularity: str | None = None
    geozones: List[str] | None = None
    last_modified: date | None = None

    organization: str | None = None
    organization_name: str | None = None
    orga_sp: int | None = None
    orga_followers: int | None = None

    elements_titles: str | None = None

    def __post_init__(self):
        if isinstance(self.created_at, str):
            self.created_at = isoparse(self.created_at)
        if isinstance(self.last_modified, str):
            self.last_modified = isoparse(self.last_modified)

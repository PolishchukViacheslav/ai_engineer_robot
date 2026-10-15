from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class TaskType(StrEnum):
    bug = "bug"
    feature = "feature"
    docs = "docs"
    question = "question"
    security = "security"


class Network(StrEnum):
    mainnet = "mainnet"
    testnet = "testnet"
    both = "both"
    not_specified = "not_specified"


class Language(StrEnum):
    uk = "uk"
    en = "en"
    mixed = "mixed"


class ApiKind(StrEnum):
    endpoint = "endpoint"
    sdk_method = "sdk_method"
    ws_subscription = "ws_subscription"
    action_type = "action_type"


class ApiRelation(StrEnum):
    new_requested = "new_requested"
    broken = "broken"
    docs_unclear = "docs_unclear"


class ApiReference(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(
        description="API name exactly as written, e.g. 'userSetAbstraction' or 'POST /exchange'"
    )
    kind: ApiKind
    relation: ApiRelation = Field(description="Why this API is mentioned in the issue")


class TechnicalTask(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(description="Short title of the issue")
    task_type: TaskType
    summary: str = Field(description="1-2 sentence summary of the problem or request")
    component: str | None = Field(description="Affected SDK area, or null if not stated")
    sdk_version: str | None = Field(description="SDK version if mentioned, else null")
    network: Network
    expected_behavior: str | None = Field(
        description="What the reporter expects to happen, or null"
    )
    api_references: list[ApiReference] = Field(description="APIs mentioned; empty list if none")
    source_language: Language

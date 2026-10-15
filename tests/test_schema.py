import pytest
from pydantic import ValidationError

from src.extraction.schema import TechnicalTask


def make(**overrides):
    data = {
        "title": "Add support for TWAP orders",
        "task_type": "feature",
        "summary": "Reporter asks for TWAP order support in the SDK.",
        "component": None,
        "sdk_version": None,
        "network": "not_specified",
        "expected_behavior": None,
        "api_references": [],
        "source_language": "en",
    }
    data.update(overrides)
    return data


def test_minimal_valid():
    TechnicalTask.model_validate(make())


def test_valid_with_api_reference():
    task = TechnicalTask.model_validate(
        make(
            task_type="bug",
            network="testnet",
            sdk_version="0.22.0",
            api_references=[
                {"name": "userSetAbstraction", "kind": "action_type", "relation": "broken"}
            ],
        )
    )
    assert task.api_references[0].name == "userSetAbstraction"


def test_valid_mixed_language_with_nulls():
    TechnicalTask.model_validate(make(source_language="mixed", component=None))


def test_invalid_enum_value_rejected():
    with pytest.raises(ValidationError):
        TechnicalTask.model_validate(make(task_type="urgent"))

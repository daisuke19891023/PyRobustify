from typing import Any

import pytest

from tools.core.base_tool import BaseTool


class DummyTool(BaseTool):
    def run(self, target: str) -> dict[str, Any]:
        return {"status": "success", "message": f"Processed {target}"}

    def parse_output(self, output: str) -> dict[str, Any]:
        return {"parsed": output}


@pytest.fixture
def dummy_tool() -> DummyTool:
    return DummyTool("DummyTool", {"key": "value"})


def test_base_tool_initialization(dummy_tool: DummyTool) -> None:
    assert dummy_tool.name == "DummyTool"
    assert dummy_tool.config == {"key": "value"}

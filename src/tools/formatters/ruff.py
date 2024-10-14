from typing import Any

from tools.core.base_tool import BaseTool


class RuffFormatter(BaseTool):
    def __init__(self, config: dict[str, Any] | None = None) -> None:
        super().__init__(name="Ruff Formatter", config=config)

    def run(self, target: str) -> dict[str, Any]:
        raise NotImplementedError

    def parse_output(self, output: str) -> dict[str, Any]:
        raise NotImplementedError

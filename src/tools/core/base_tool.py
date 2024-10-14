# core/base_tool.py

from abc import ABC, abstractmethod
from typing import Any

ConfigValue = str | int | float | bool | list[Any] | dict[str, Any] | None


class BaseTool(ABC):
    def __init__(self, name: str, config: dict[str, ConfigValue] | None = None) -> None:
        self.name = name
        self.config = config or {}

    @abstractmethod
    def run(self, target: str) -> dict[str, ConfigValue]:
        """
        Run the tool on the target.

        :param target: Path to the target file or directory
        :return: Dictionary containing the results
        """

    @abstractmethod
    def parse_output(self, output: str) -> dict[str, ConfigValue]:
        """
        Parse the output of the tool.

        :param output: Raw output from the tool
        :return: Dictionary containing the parsed results
        """

    def get_config(
        self, key: str, default: ConfigValue | None = None
    ) -> ConfigValue | None:
        """
        Get a configuration value.

        :param key: Configuration key
        :param default: Default value if key is not found
        :return: Configuration value
        """
        return self.config.get(key, default)

    def set_config(self, key: str, value: ConfigValue) -> None:
        """
        Set a configuration value.

        :param key: Configuration key
        :param value: Configuration value
        """
        self.config[key] = value

    def __str__(self) -> str:
        return f"{self.name} Tool"

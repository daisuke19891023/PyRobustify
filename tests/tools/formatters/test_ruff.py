import pytest

from tools.formatters.ruff import RuffFormatter


@pytest.fixture
def ruff_formatter() -> RuffFormatter:
    return RuffFormatter()


def test_ruff_formatter_init(ruff_formatter: RuffFormatter) -> None:
    assert ruff_formatter.name == "Ruff Formatter"
    assert isinstance(ruff_formatter.config, dict)

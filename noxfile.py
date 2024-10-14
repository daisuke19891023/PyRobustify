import platform
import sys
from pathlib import Path

import nox
from nox.sessions import Session


def constraints(session: Session) -> Path:
    # Automatically create constraints file name
    filename = f"python{session.python}-{sys.platform}-{platform.machine()}.txt"
    return Path("constraints", filename)


@nox.session(python=["3.12"], venv_backend="uv")
def lock(session: Session) -> None:
    filename = constraints(session)
    filename.parent.mkdir(exist_ok=True)
    session.run(
        "uv",
        "pip",
        "compile",
        "pyproject.toml",
        "--upgrade",
        "--quiet",
        "--all-extras",
        f"--output-file={filename}",
    )


@nox.session(python=["3.12"])
def lint(session: Session) -> None:
    session.install("-c", constraints(session).as_posix(), "ruff")
    session.run("ruff", "check")


@nox.session(python=["3.12"])
def formatting(session: Session) -> None:
    session.install("-c", constraints(session).as_posix(), "ruff")
    session.run("ruff", "format")


@nox.session(python=["3.12"])
def typing(session: Session) -> None:
    session.install("-c", constraints(session).as_posix(), ".[typing]")
    session.run("mypy")


@nox.session(python=["3.12"])
def test(session: Session) -> None:
    session.install("-c", constraints(session).as_posix(), ".[tests]")
    session.run("pytest")

"""Pre Prompt hook."""

import subprocess
import sys

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m"
INFO = "\x1b[1;34m"
HINT = "\x1b[3;35m"
SUCCESS = "\x1b[1;32m"
ERROR = "\x1b[1;31m"
MSG_DELIMITER = "=" * 80
MSG_DELIMITER_2 = "-" * 80
SEMVER_PATTERN = r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"  # noQA
PEP404_PATTERN = r"^(\d+!)?(\d+)(\.\d+)+([\.\-\_])?((a(lpha)?|b(eta)?|c|r(c|ev)?|pre(view)?)\d*)?(\.?(post|dev)\d*)?$"  # noQA


def _error(msg: str) -> str:
    """Format error message."""
    return f"{ERROR}{msg}{TERMINATOR}"


def _success(msg: str) -> str:
    """Format success message."""
    return f"{SUCCESS}{msg}{TERMINATOR}"


def _warning(msg: str) -> str:
    """Format warning message."""
    return f"{WARNING}{msg}{TERMINATOR}"


def _info(msg: str) -> str:
    """Format info message."""
    return f"{INFO}{msg}{TERMINATOR}"


SUPPORTED_NODE_VERSIONS = [
    "18",
    "19",
    "20",
    "21",
    "22",
]


def _get_command_version(cmd: str) -> str:
    """Get version of a command."""
    try:
        raw_version = (
            subprocess.run([cmd, "--version"], capture_output=True)
            .stdout.decode()
            .strip()
        )
    except FileNotFoundError:
        raw_version = ""
    return raw_version


def check_node_version() -> str:
    """Check if Node version is supported."""
    raw_version = _get_command_version("node")
    major_version = raw_version[1:3] if raw_version else ""
    return (
        ""
        if major_version in SUPPORTED_NODE_VERSIONS
        else f"Node version is not supported: Got {raw_version}"
    )


def check_git_version() -> str:
    """Check if git is installed."""
    raw_version = _get_command_version("git")
    return "" if raw_version else "Git not found."


def sanity_check() -> bool:
    """Run sanity checks on the system."""
    checks = {
        "Node": {"func": check_node_version, "level": "error"},
        "git": {"func": check_git_version, "level": "warning"},
    }
    has_error = False
    print("Sanity checks")
    print(f"{MSG_DELIMITER_2}")
    total_checks = len(checks)
    for idx, (title, check_info) in enumerate(checks.items()):
        func = check_info["func"]
        status = func()
        level = check_info["level"]
        if not status:
            msg = f"{_success('✓')}"
        elif level == "error":
            has_error = True
            msg = f"{_error(status)}"
        else:
            msg = f"{_warning(status)}"
        print(f"  [{idx+1}/{total_checks}] {title}: {msg}")
    return not (has_error)


def main():
    """Validate context."""
    print("")
    print(f"{ _info('Cookiecutter Volto Add-on ')}")
    print(f"{MSG_DELIMITER}")
    print("")
    if not sanity_check():
        sys.exit(1)
    print("")
    print(f"Add-on details")
    print(f"{MSG_DELIMITER_2}")
    print("")


if __name__ == "__main__":
    main()

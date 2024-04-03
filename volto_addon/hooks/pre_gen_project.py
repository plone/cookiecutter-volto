"""Pre generation hook."""

import re
import sys
from pathlib import Path
from textwrap import dedent
from typing import List

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m"
INFO = "\x1b[1;34m"
HINT = "\x1b[3;35m"
SUCCESS = "\x1b[1;32m"
ERROR = "\x1b[1;31m"
MSG_DELIMITER = "=" * 80
MSG_DELIMITER_2 = "-" * 80

output_path = Path().resolve()

context = {
    "addon_name": "{{ cookiecutter.addon_name }}",
    "addon_title": "{{ cookiecutter.addon_title }}",
    "description": "{{ cookiecutter.description }}",
    "author": "{{ cookiecutter.author }}",
    "email": "{{ cookiecutter.email }}",
    "github_organization": "{{ cookiecutter.github_organization }}",
    "npm_package_name": "{{ cookiecutter.npm_package_name }}",
    "noaddon": "{{ cookiecutter.noaddon }}",
}


def _error(msg: str) -> str:
    """Format error message."""
    return f"{ERROR}{msg}{TERMINATOR}"


def _success(msg: str) -> str:
    """Format success message."""
    return f"{SUCCESS}{msg}{TERMINATOR}"


def _info(msg: str) -> str:
    """Format info message."""
    return f"{INFO}{msg}{TERMINATOR}"


def validate_not_empty(value: str) -> str:
    """Value should not be empty."""
    return "" if value.strip() else "should be provided"


def validate_addon_name(value: str) -> str:
    """Validate addon_name is valid."""
    pattern = "^[a-z0-9-~][a-z0-9-._~]*$"
    if not re.match(pattern, value):
        return "Invalid addon_name"


def validate_npm_package_name(value: str) -> str:
    """Validate npm_package_name is valid."""
    pattern = "^(@[a-z0-9-~][a-z0-9-._~]*\/)?[a-z0-9-~][a-z0-9-._~]*$"
    if not re.match(pattern, value):
        return "Invalid npm_package_name"


VALIDATORS = {
    name: func for name, func in locals().items() if name.startswith("validate_")
}


def check_errors(data: dict) -> List[str]:
    """Check for errors in the provided data."""
    errors = []
    for key, value in data.items():
        func = VALIDATORS.get(f"validate_{key}", validate_not_empty)
        error = func(value)
        if error:
            errors.append(f"  - {key}: {_error(error)}")
    return errors


def main():
    """Validate context."""
    success = True
    value_errors = check_errors(context)
    print("")

    print(f"{ _info('{{ cookiecutter.addon_title }} generation')}")
    print(f"{MSG_DELIMITER_2}")
    if value_errors:
        print("Value errors prevent running cookiecutter")
        for error in value_errors:
            print(error)
        success = False
    else:
        msg = dedent(
            f"""
            Summary:
              - Volto version: {_info('{{ cookiecutter.__version_plone_volto }}')}
              - Output folder: {_info(output_path)}
        """
        )

        print(msg)
    if not success:
        print(f"{MSG_DELIMITER}")
        sys.exit(1)


if __name__ == "__main__":
    main()

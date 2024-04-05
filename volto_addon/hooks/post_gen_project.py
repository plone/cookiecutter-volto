"""Post generation hook."""

import pathlib
import shutil
import subprocess
import sys
from textwrap import dedent

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m"
INFO = "\x1b[1;34m"
HINT = "\x1b[3;35m"
SUCCESS = "\x1b[1;32m"
ERROR = "\x1b[1;31m"
MSG_DELIMITER = "=" * 80

context = {
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


def run_cmd(command: str, shell: bool, cwd: str) -> bool:
    proc = subprocess.run(command, shell=shell, cwd=cwd, capture_output=True)
    if proc.returncode:
        # Write errors to the main process stderr
        print(_error(f"\nError while running {command}:"), file=sys.stderr)
        sys.stderr.buffer.write(proc.stderr)
        print("\n", file=sys.stderr)
    return False if proc.returncode else True


def remove(filepath):
    filepath = pathlib.Path(filepath)
    if filepath.is_file():
        filepath.unlink()
    elif filepath.is_dir():
        shutil.rmtree(filepath)


def main():
    """Final fixes."""
    if context["noaddon"] != "False":
        remove("packages/{{ cookiecutter.addon_name }}")

    print(f"{MSG_DELIMITER}")
    print("")
    print(f"{MSG_DELIMITER}")
    msg = dedent(
        f"""
        {_success('New add-on "{{ cookiecutter.addon_title }}" was generated')}

        Now, enter the generated directory and finish the install:

        cd {{ cookiecutter.addon_title }}
        make install

        start coding, and push to your organization.

        Sorry for the convenience,
        The Plone Community.
    """
    )
    print(msg)
    print(f"{MSG_DELIMITER}")


if __name__ == "__main__":
    main()

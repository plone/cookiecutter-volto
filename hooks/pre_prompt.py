"""Pre Prompt hook."""

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m"
INFO = "\x1b[1;34m"
HINT = "\x1b[3;35m"
SUCCESS = "\x1b[1;32m"
ERROR = "\x1b[1;31m"
MSG_DELIMITER = "=" * 50
MSG_DELIMITER_2 = "-" * 50


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


TEXT = """
                 .xxxxxxxxxxxxxx.
             ;xxxxxxxxxxxxxxxxxxxxxx;
          ;xxxxxxxxxxxxxxxxxxxxxxxxxxxx;
        xxxxxxxxxx              xxxxxxxxxx
      xxxxxxxx.                    .xxxxxxxx
     xxxxxxx      xxxxxxx:            xxxxxxx
   :xxxxxx       xxxxxxxxxx             xxxxxx:
  :xxxxx+       xxxxxxxxxxx              +xxxxx:
 .xxxxx.        :xxxxxxxxxx               .xxxxx.
 xxxxx+          ;xxxxxxxx                 +xxxxx
 xxxxx              +xx.                    xxxxx.
xxxxx:                      .xxxxxxxx       :xxxxx
xxxxx                      .xxxxxxxxxx       xxxxx
xxxxx                      xxxxxxxxxxx       xxxxx
xxxxx                      .xxxxxxxxxx       xxxxx
xxxxx:                      .xxxxxxxx       :xxxxx
.xxxxx              ;xx.       ...          xxxxx.
 xxxxx+          :xxxxxxxx                 +xxxxx
 .xxxxx.        :xxxxxxxxxx               .xxxxx.
  :xxxxx+       xxxxxxxxxxx              ;xxxxx:
   :xxxxxx       xxxxxxxxxx             xxxxxx:
     xxxxxxx      xxxxxxx;            xxxxxxx
      xxxxxxxx.                    .xxxxxxxx
        xxxxxxxxxx              xxxxxxxxxx
          ;xxxxxxxxxxxxxxxxxxxxxxxxxxxx+
             ;xxxxxxxxxxxxxxxxxxxxxx;
                 .xxxxxxxxxxxxxx.
"""


def main():
    """Validate context."""
    print(f"{MSG_DELIMITER}")
    print(f"{ _info(TEXT)}")
    print(f"{MSG_DELIMITER}")


if __name__ == "__main__":
    main()

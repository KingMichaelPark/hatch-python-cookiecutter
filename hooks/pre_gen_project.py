import re
import sys
from shutil import which


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""

    return which(name) is not None


def check_valid_module_name():
    MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

    module_name = "{{ cookiecutter.project_slug}}"

    if not re.match(MODULE_REGEX, module_name):
        print(
            f"""
        ERROR: The project slug ({module_name}) is not a valid Python module name.
        Please do not use a - and use _ instead
        """
        )

        # Exit to cancel project
        sys.exit(1)


if __name__ == "__main__":
    check_valid_module_name()

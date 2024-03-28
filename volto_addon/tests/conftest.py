"""Pytest configuration."""
import re
from copy import deepcopy
from pathlib import Path
from typing import List

import pytest


@pytest.fixture(scope="session")
def variable_pattern():
    return re.compile("{{( ?cookiecutter)[.](.*?)}}")


@pytest.fixture(scope="session")
def context() -> dict:
    """Cookiecutter context."""
    return {
        "addon_name": "volto-addon",
        "addon_title": "Volto Add-on",
        "description": "Add new features to your Volto Project.",
        "github_organization": "collective",
        "npm_package_name": "@plone-collective/volto-addon",
        "author": "Plone Collective",
        "email": "collective@plone.org",
    }


@pytest.fixture(scope="session")
def context_no_npm_organization(context) -> dict:
    """Cookiecutter context without a NPM organization."""
    new_context = deepcopy(context)
    new_context["npm_package_name"] = "volto-addon"
    return new_context


@pytest.fixture(scope="session")
def bad_context() -> dict:
    """Cookiecutter context with invalid data."""
    return {
        "addon_name": "volto addon",
        "addon_title": "Volto Add-on",
        "description": "Add new features to your Volto Project.",
        "github_organization": "collective",
        "npm_package_name": "plone-collective/volto-addon",
        "author": "Plone Collective",
        "email": "collective@plone.org",
    }


@pytest.fixture
def build_files_list():
    def func(root_dir: Path) -> List[Path]:
        """Build a list containing absolute paths to the generated files."""
        return [path for path in Path(root_dir).glob("*") if path.is_file()]

    return func


@pytest.fixture(scope="session")
def cutter_result(cookies_session, context):
    """Cookiecutter result."""
    return cookies_session.bake(extra_context=context)

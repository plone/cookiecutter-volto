"""Pytest configuration."""

import json
import logging
import re
from copy import deepcopy
from pathlib import Path
from typing import List

import jsonschema
import pytest
import requests
from ruamel.yaml import YAML

logger = logging.getLogger("cookiecuter-volto-volto_addon")
yaml = YAML()


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


@pytest.fixture(scope="session")
def json_schemas() -> dict:
    """Validate files."""
    remote_schemas = [
        ["package.json", "https://json.schemastore.org/package.json"],
        ["tsconfig.json", "https://json.schemastore.org/tsconfig.json"],
        ["github-workflow", "https://json.schemastore.org/github-workflow.json"],
    ]
    schemas = {}
    for name, url in remote_schemas:
        response = requests.get(url)
        if response.status_code == 200:
            schemas[name] = response.json()
    return schemas


@pytest.fixture
def validate_schema(json_schemas):
    """Validate a file against a known JSON Schema."""

    def func(file_path: Path, schema_name):
        validation = False
        # Remove . from file extension
        extension = file_path.suffix[1:]
        raw = file_path.read_text()
        if extension in ("yaml", "yml"):
            data = yaml.load(raw)
        elif extension in ("json"):
            data = json.loads(raw)
        else:
            data = {}
        schema = json_schemas[schema_name]
        try:
            jsonschema.validate(data, schema)
        except jsonschema.ValidationError as exc:
            logger.error(f"Validation of {file_path} failed {exc}")
            validation = False
        else:
            validation = True
        return validation

    return func

# {{ cookiecutter.addon_title }} ({{ cookiecutter.npm_package_name }})

{{ cookiecutter.description }}

[![npm](https://img.shields.io/npm/v/{{ cookiecutter.npm_package_name }})](https://www.npmjs.com/package/{{ cookiecutter.npm_package_name }})
[![](https://img.shields.io/badge/-Storybook-ff4785?logo=Storybook&logoColor=white&style=flat-square)](https://kitconcept.github.io/{{ cookiecutter.addon_name }}/)
[![Code analysis checks](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.addon_name }}/actions/workflows/code.yml/badge.svg)](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.addon_name }}/actions/workflows/code.yml)
[![Unit tests](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.addon_name }}/actions/workflows/unit.yml/badge.svg)](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.addon_name }}/actions/workflows/unit.yml)

## Features

<!-- List your awesome features here -->

## Install

Create a new Volto project (you can skip this step if you already have one):

```
npm install -g yo @plone/generator-volto
yo @plone/volto my-volto-project --addon {{ cookiecutter.npm_package_name }}
cd my-volto-project
```

Add `{{ cookiecutter.npm_package_name }}` to your package.json:

```JSON
"addons": [
    "{{ cookiecutter.npm_package_name }}"
],

"dependencies": {
    "{{ cookiecutter.npm_package_name }}": "*"
}
```

Download and install the new add-on by running:

```
yarn install
```

Start volto with:

```
yarn start
```

### Test it

Go to http://localhost:3000/, login and check the awesome new features.

## Development

The development of this add-on is done in isolation using a new approach using pnpm workspaces and latest `mrs-developer` and other Volto core improvements.
For this reason, it only works with pnpm and Volto 18 (currently in alpha)

### Requisites

- Volto 18
- pnpm as package manager

### Make convenience commands

Run `make help` to list the available commands.

```text
help                                 Show this help
install                              Installs the dev environment using mrs-developer
i18n                                 Sync i18n
format                               Format codebase
lint                                 Lint Codebase
test                                 Run unit tests
test-ci                              Run unit tests in CI
storybook-start                      Start Storybook server on port 6006
storybook-build                      Build Storybook
start-backend-docker                 Starts a Docker-based backend for developing
start-test-acceptance-frontend-dev   Start acceptance frontend in dev mode
start-test-acceptance-frontend       Start acceptance frontend in prod mode
start-test-acceptance-server         Start acceptance server
test-acceptance                      Start Cypress in interactive mode
test-acceptance-headless             Run cypress tests in headless mode for CI
```

### Development Environment Setup

Install package requirements

```shell
make install
pnpm i
```

### Start developing

Run (in separate terminal sessions)

Start backend server

```shell
make start-backend-docker
```

Start frontend

```shell
pnpm start
```

### Linting

Run ESlint, Prettier and Stylelint

```shell
make lint
```

### Formatting

Run ESlint, Prettier and Stylelint in fix mode

```shell
make format
```

### i18n

Extract the i18n messages to locales

```shell
make i18n
```

### Unit tests

Run unit tests

```shell
make test
```

### Run Cypress tests

Run (in separate terminal sessions)

Start the frontend in dev mode

```shell
make start-test-acceptance-frontend-dev
```

Start the backend acceptance server

```shell
make start-test-acceptance-server
```

Start the Cypress interactive test runner

```shell
make test-acceptance
```

## License

The project is licensed under the MIT license.

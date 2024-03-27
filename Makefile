SHELL := /bin/bash
CURRENT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))


# We like colors
# From: https://coderwall.com/p/izxssa/colored-makefile-for-golang-projects
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr0`
YELLOW=`tput setaf 3`

.PHONY: all
all: bin/cookiecutter

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
.PHONY: help
help: ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## Clean
	rm -rf bin include lib lib64 pyvenv.cfg .Python

bin/cookiecutter: ## Create virtualenv and install dependencies
	@echo "$(GREEN)==> Setup Virtual Env$(RESET)"
	python3 -m venv .
	bin/pip install pip --upgrade
	bin/pip install -r requirements.txt --upgrade

.PHONY: format
format: bin/cookiecutter ## Format code
	@echo "$(GREEN)==> Formatting codebase $(RESET)"
	bin/black hooks
	bin/isort hooks
	$(MAKE) -C "./volto_addon/" format

.PHONY: test
test: bin/cookiecutter ## Test all cookiecutters
	@echo "$(GREEN)==> Test all cookiecutters$(RESET)"
	$(MAKE) -C "./volto_addon/" test

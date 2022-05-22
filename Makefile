#!/usr/bin/env make

# Change this to be your variant of the python command
PYTHON ?= python # python3 py

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

# To make targets in each directory under the src/
define FOREACH
    for DIR in src/*; do \
        $(MAKE) -C $$DIR $(1); \
    done
endef

all:


# ---------------------------------------------------------
# Setup a venv and install packages.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	rm -f .coverage *.pyc
	rm -rf src/__pycache__
	rm -rf htmlcov

clean-doc:
	rm -rf doc

clean-venv:
	rm -rf .venv

clean-all: clean clean-doc


# ---------------------------------------------------------
# Test all the code at once.
#
pylint:
	@$(call MESSAGE,$@)
	-cd src && $(PYTHON) -m pylint *.py

flake8:
	@$(call MESSAGE,$@)
	-cd src && $(PYTHON) -m flake8 *.py

lint: flake8 pylint
# ---------------------------------------------------------
# Work with unit test and code coverage.
#
unittest:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m unittest discover src

coverage:
	@$(call MESSAGE,$@)
	coverage run -m unittest discover src
	coverage html
	coverage report -m

test: lint coverage
#----------------------------------------------------------
# DOCUMENTATION 
#
.PHONY: pydoc
pydoc:
	@$(call MESSAGE,$@)
	# This does not work on Windows installed Python
	$(PYTHON) -m pydoc -w "$(PWD)"
	install -d doc/pydoc
	mv *.html doc/pydoc

pdoc:
	@$(call MESSAGE,$@)
	pdoc --force --html --output-dir doc/api src/*.py

pyreverse:
	@$(call MESSAGE,$@)
	install -d doc/uml
	pyreverse src/*.py
	dot -Tpng classes.dot -o doc/uml/classes.png
	dot -Tpng packages.dot -o doc/uml/packages.png
	rm -f classes.dot packages.dot

doc: pdoc pyreverse #pydoc sphinx
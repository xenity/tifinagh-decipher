MAKESHELL ?= /bin/bash

setup-python:
	@echo "Installing python virtual environment..."
	python3 -m venv venv
	. venv/bin/activate && python -m pip install --upgrade pip -r requirements.txt

shell: 
	@echo "Use command 'exit' to kill this shell, or hit <Ctl-D>"
	. venv/bin/activate && ${MAKESHELL}

search: 
	@python src/main.py
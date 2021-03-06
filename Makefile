REQUIREMENTS_LOCAL_IN = requirements/local.in


pip-compile:
	## Update requirements/*.txt with latest packages from requirements/*.in
	echo "Installing/upgrading pip-tools..."
	pip install -qU pip-tools

	echo "Upgrading local packages..."
	pip-compile -U requirements/dev.in
	pip-compile -U requirements/heroku.in
	pip-compile -U requirements/production.in

	echo "Compiling test requirements..."
	pip-compile -U -o requirements/test.txt requirements/production.in requirements/test.in
ifneq (, $(wildcard $(REQUIREMENTS_LOCAL_IN)))
	pip-compile -U $(REQUIREMENTS_LOCAL_IN)
endif


install-dev-requirements:
	# Install requirements for a local development environment
	echo "Installing dev requirements..."
	pip install -qU pip-tools
	pip-sync requirements/*.txt


test:
	# Run the complete test suite + coverage report
	coverage run --source src --omit '*migrations*' -m pytest
	coverage report

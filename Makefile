.SILENT: fmt check lint

fmt:
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		flake8_datetime_utcnow tests
	isort --profile black .
	black .

check:
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		-c \
		flake8_datetime_utcnow tests
	isort --profile black -c .
	black --check .

lint:
	mypy flake8_datetime_utcnow tests
	flake8 .

test:
	pytest -x --cov=core --cov=flake8_datetime_utcnow --cov-fail-under=90

.SILENT: fmt check

fmt:
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		setup.py tests flake8_datetime_utcnow
	isort --profile black .
	black .

check:
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		-c \
		setup.py tests flake8_datetime_utcnow
	isort --profile black -c .
	black --check .

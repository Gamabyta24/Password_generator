install:
	poetry install
generate-pass:
	poetry run generate
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 pass_gen/
format:
	poetry run black pass_gen/

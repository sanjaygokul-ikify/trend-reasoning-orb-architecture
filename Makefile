CI: ci

ci:
	poetry install
	poetry run pytest
	docker-compose build
	docker-compose run test

doc: mkdocs build

all: ci doc
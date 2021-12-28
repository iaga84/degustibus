clean:
	find ./ . -name '*.pyc' -type f -delete
	rm -rf tests/__pycache__
	docker 2>/dev/null 1>&2 rmi -f python:3.7 || true
	$(eval PYTHON_IMAGES := $(shell docker images -q python))
	$(eval PROJECT_IMAGES := $(shell docker images -q wfp-api-integrator))
	docker 2>/dev/null 1>&2 rmi -f $(PYTHON_IMAGES) || true
	docker 2>/dev/null 1>&2 rmi -f $(PROJECT_IMAGES) || true
	docker system prune -f

build: clean
	docker build --no-cache -t iaga/degustibus .

push: build
	docker push iaga/degustibus:latest

run: build
	docker run -p 6969:6969 iaga/degustibus:latest

dashboard: clean
	cd OpenSearch-Dashboard && docker build -t iaga/opensearch-dashboard .
	docker push iaga/opensearch-dashboard:latest


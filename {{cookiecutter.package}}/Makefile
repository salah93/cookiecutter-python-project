build: clean
	python -m build

deploy: build
	twine upload dist/*

deploy-test: build
	twine upload -r testpypi dist/*

clean:
	rm -rf dist build
	find . -name "__pycache__" -print0 | xargs -0 -I{} rm -rf {}

.PHONY: clean deploy deploy-test build

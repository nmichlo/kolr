build: clean
	python3 setup.py sdist bdist_wheel

test_upload: build
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload: build
	python3 -m twine upload --repository-url https://pypi.org/legacy/ dist/*

clean:
	rm -rf ./build ./dist ./kolr.egg-info
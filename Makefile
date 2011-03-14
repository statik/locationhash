check: lint
	@nosetests --config=.nosecfg

lint:
	@find . -name \*.py -exec flake8 {} \; 

info:
	@git shortlog -2
	@echo
	@echo "Lines of application code"
	@find . -name \*py | grep -v test_ | xargs cat | wc -l
	@echo
	@echo "Lines of test code:"
	@find . -name \*py | grep test_ | xargs cat | wc -l
	@echo
	@coverage report --omit="test_*"

clean:
	find . -name \*pyc -exec rm {} \;
	rm -rf cover
	rm -rf dist
	rm -rf MANIFEST

autotest: #TODO figure out autotest crashing on snow leopard
	autonose --console --info --config=.nosecfg

dist:
	python setup.py sdist
	cd dist; tar tvf *.tar.gz

.PHONY: dist

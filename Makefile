export ROOTDIR ?= $(shell git rev-parse --show-toplevel)
export DBDIR ?= $(ROOTDIR)/tmp/mongo

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

$(DBDIR):
	mkdir -p $(DBDIR)

start-db: $(DBDIR)
	@mongod --pidfilepath $(DBDIR) --logpath $(DBDIR)/mongo.log --logappend --fork --dbpath $(DBDIR) --noauth

stop-db: $(DBDIR)
	@mongo admin util/shutdown.js

.PHONY: dist autotest clean info lint check start-db stop-db
.NOTPARALLEL:

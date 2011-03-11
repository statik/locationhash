check:
	@nosetests --config=.nosecfg

info:
	@git describe
	@echo
	@echo "Lines of application code"
	@find . -name \*py | grep -v test_ | xargs cat | wc -l
	@echo
	@echo "Lines of test code:"
	@find -name \*py | grep test_ | xargs cat | wc -l

clean:
	find . -name \*pyc -exec rm {} \;
	rm -rf cover

autotest: #TODO figure out autotest crashing on snow leopard
	autonose --console --info --config=.nosecfg

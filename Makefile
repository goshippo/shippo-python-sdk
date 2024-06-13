include Makefile-extras

.PHONY: *
SHELL := bash

publish:
	./scripts/publish.sh

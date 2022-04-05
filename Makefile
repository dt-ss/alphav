#!/bin/bash

.PHONY: test

test:
	PYTHONPATH="." && pytest -s
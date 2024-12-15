# Copyright (C) 2024 nggit

NAME = pspparse

LEX = flex
PYTHON := $(shell command -v python3 || command -v python)

all: psp_parser.c $(NAME).so test

psp_parser.c: psp_parser.l
	@rm -f psp_parser.c
	$(LEX) -R -opsp_parser.c --header-file=include/psp_flex.h psp_parser.l

$(NAME).so: psp_parser.c
	$(PYTHON) setup.py build_ext --inplace

clean:
	rm -rf build $(NAME).*.so

test:
	$(PYTHON) tests.py

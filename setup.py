# Copyright (c) 2024 nggit

from setuptools import setup, Extension


pspparse = Extension(
    'pspparse',
    sources=[
        'pspparse.c',
        'psp_string.c',
        'psp_parser.c',
    ],
    include_dirs=['include']
)


setup(
    ext_modules=[pspparse]
)

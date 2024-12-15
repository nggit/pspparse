# Copyright (c) 2024 nggit

from setuptools import setup, Extension


with open('README.md', 'r') as f:
    long_description = f.read()

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
    name='pspparse',
    version='0.0.0',
    license='Apache Software License',
    author='nggit',
    author_email='contact@anggit.com',
    description=(
        'pspparse is a Python module containing a PSP parser '
        'extracted from the mod_python project.'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nggit/pspparse',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
    ext_modules=[pspparse]
)

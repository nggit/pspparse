pspparse
========

**pspparse** is a Python module containing a PSP parser extracted from the [mod_python](https://modpython.org/) project.

It is not meant for console games, but [Python Server Pages](https://modpython.org/live/mod_python-3.3.1/doc-html/pyapi-psp.html). I have an idea to use it on [httpout](https://github.com/nggit/httpout).

Build the module
----------------

```
$ make
```

Usage
-----

```python
from pspparse import parse_string

source = parse_string(b'Hello, <%=__name__%>!')
```

The result is the following source code.

```python
"print('''Hello, ''', end=''); print(__name__, end=''); print('''!''', end='')"
```

Changes that have been made from the original
---------------------------------------------

- Rename module from `_psp` to `pspparse`
- Change `req.write()` to `print()`
- Add an alias for `parsestring`, `parse_string`

License
-------

Apache License, Version 2.0

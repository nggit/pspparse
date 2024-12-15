# Copyright (C) 2024 nggit

import unittest
from pspparse import parse_string


class TestPSPParser(unittest.TestCase):
    def test_code_empty(self):
        self.assertEqual(
            parse_string(b"<%%>"),
            "print('''''', end='');; print('''''', end='')\n"
        )

    def test_code_inline(self):
        self.assertEqual(
            parse_string(b"<%print('Hello')%>"),
            "print('''''', end='');print('Hello'); print('''''', end='')\n"
        )

    def test_code_inline_spaces_between(self):
        self.assertEqual(
            parse_string(b"<% print('Hello') %>"),
            "print('''''', end=''); print('Hello') ; print('''''', end='')\n"
        )

    def test_code_newline(self):
        self.assertEqual(
            parse_string(b"<% print('Hello')\n%>"),
            "print('''''', end=''); print('Hello')\nprint('''''', end='')\n"
        )

    def test_code_colon(self):
        self.assertEqual(
            parse_string(b"<% for i in range(10):\n%>"),
            "print('''''', end=''); for i in range(10):\n\t"
            "print('''''', end='')\n"
        )

    def test_expr_empty(self):
        self.assertEqual(
            parse_string(b"<%=%>"),
            "print('''''', end=''); print(, end=''); print('''''', end='')\n"
        )

    def test_expr(self):
        self.assertEqual(
            parse_string(b"<%=name%>"),
            "print('''''', end=''); print(name, end=''); "
            "print('''''', end='')\n"
        )

    def test_expr_inline_spaces_between(self):
        self.assertEqual(
            parse_string(b"<%= name %>"),
            "print('''''', end=''); print( name , end=''); "
            "print('''''', end='')\n"
        )

    def test_expr_newline(self):
        self.assertEqual(
            parse_string(b"<%= name\n%>"),
            "print('''''', end=''); print( name\n, end=''); "
            "print('''''', end='')\n"
        )


if __name__ == "__main__":
    unittest.main()

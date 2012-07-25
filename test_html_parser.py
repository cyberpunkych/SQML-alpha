#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import html_parser


class TestTagsParser(unittest.TestCase):
    def setUp(self):
        self.html_parser = html_parser.Parser()

    def test_content_1(self):
        data = '<div class="a">A</div>'
        query = 'SELECT @@content FROM div'

        self.html_parser.load(data)
        self.html_parser.query(query)

        self.assertEqual(
            self.html_parser.result,
            [['A']]
        )

    def test_content_2(self):
        data = '<div class="a">A</div><div class="b">B</div><div class="c">C</div>'
        query = 'SELECT @@content FROM div'

        self.html_parser.load(data)
        self.html_parser.query(query)

        self.assertEqual(
            self.html_parser.result,
            [['A'], ['B'], ['C'], ]
        )

    def test_content_with_nested_1(self):
        data = '<div class="outer"><div class="a">A</div><div class="b">B</div><div class="c">C</div></div>'
        query = 'SELECT @@content FROM div'

        self.html_parser.load(data)
        self.html_parser.query(query)

        self.assertEqual(
            self.html_parser.result,
            [['<div class="a">A</div><div class="b">B</div><div class="c">C</div>'], ['A'], ['B'], ['C'], ]
        )

    def test_content_with_nested_2(self):
        data = '<div class="outer"><p class="a">A</p><p class="b">B</p><p class="c">C</p></div>'
        query = 'SELECT @@content FROM div'

        self.html_parser.load(data)
        self.html_parser.query(query)

        self.assertEqual(
            self.html_parser.result,
            [['<p class="a">A</p><p class="b">B</p><p class="c">C</p>']]
        )

    def test_content_with_condition_1(self):
        data = '<div class="a">A</div><div class="a">B</div><div class="a">C</div>'
        query = 'SELECT @@content FROM div WHERE @class==\'a\''

        self.html_parser.load(data)
        self.html_parser.query(query)

        self.assertEqual(
            self.html_parser.result,
            [['A'], ['B'], ['C'], ]
        )

    def test_content_with_condition_2(self):
        data = '<div class="a">A</div><div class="a">B</div><div class="a">C</div>'
        query = 'SELECT @@content FROM div WHERE @class==\'not-existent\''

        self.html_parser.load(data)
        self.html_parser.query(query)

        self.assertEqual(
            self.html_parser.result,
            []
        )

    def test_content_with_condition_3(self):
        data = '<div class="a">A</div><div class="a">B</div><div class="a">C</div>'
        query = 'SELECT @@content FROM not_existent WHERE @class==\'a\''

        self.html_parser.load(data)
        self.html_parser.query(query)

        self.assertEqual(
            self.html_parser.result,
            []
        )


class TestQueryParser(unittest.TestCase):
    def setUp(self):
        self.html_parser_1 = html_parser.Parser()
        self.html_parser_2 = html_parser.Parser()

    def test_exact_queries(self):
        data = '<div class="a">A</div>'

        query = 'SELECT @@content FROM div'

        self.html_parser_1.load(data)
        self.html_parser_2.load(data)

        self.html_parser_1.query(query)
        self.html_parser_2.query(query)

        self.assertEqual(
            self.html_parser_1.result,
            self.html_parser_2.result
        )

    def test_queries_with_whitespace_1(self):
        data = '<div class="a">A</div>'

        query = 'SELECT @@content FROM             div                 '

        self.html_parser_1.load(data)

        self.html_parser_1.query(query)

    def test_queries_with_whitespace_2(self):
        data = '<div class="a">A</div>'

        query_1 = 'SELECT @@content FROM div WHERE @class==\'non-existent\''
        query_2 = 'SELECT @@content FROM div   WHERE @class==\'non-existent\''

        self.html_parser_1.load(data)
        self.html_parser_2.load(data)

        self.html_parser_1.query(query_1)
        self.html_parser_2.query(query_2)

        self.assertEqual(
            self.html_parser_1.result,
            self.html_parser_2.result
        )

    def test_queries_with_whitespace_3(self):
        data = '<div class="a">A</div><div class="b">B</div>'

        query_1 = 'SELECT @@content FROM div WHERE @class==\'a\''
        query_2 = 'SELECT @@content FROM div   WHERE @class==\'a\''

        self.html_parser_1.load(data)
        self.html_parser_2.load(data)

        self.html_parser_1.query(query_1)
        self.html_parser_2.query(query_2)

        self.assertEqual(
            self.html_parser_1.result,
            self.html_parser_2.result
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)

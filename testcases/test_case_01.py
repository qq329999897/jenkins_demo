#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_case_01.py
# @time: 2020/9/15 11:45 下午

import unittest

class TestCase01(unittest.TestCase):
    def test_add(self):
        self._testMethodDoc = '测试1+1是否等于2'
        self.assertEqual(1+1,2)

    def test_sub(self):
        self._testMethodDoc = '测试1-1是否等于0'
        self.assertEqual(1-1,0)
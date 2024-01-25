# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_LRUCache_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        lruCache = program.LRUCache(3)
        lruCache.insertKeyValuePair("b", 2)
        lruCache.insertKeyValuePair("a", 1)
        lruCache.insertKeyValuePair("c", 3)
        self.assertEqual(lruCache.getMostRecentKey(), "c")
        self.assertEqual(lruCache.getValueFromKey("a"), 1)
        self.assertEqual(lruCache.getMostRecentKey(), "a")
        lruCache.insertKeyValuePair("d", 4)
        self.assertEqual(lruCache.getValueFromKey("b"), None)
        lruCache.insertKeyValuePair("a", 5)
        self.assertEqual(lruCache.getValueFromKey("a"), 5)

    def test_case_2(self):
        lruCache = program.LRUCache(1)
        lruCache.getValueFromKey('a')
        lruCache.insertKeyValuePair('a', 1)
        lruCache.getValueFromKey('a')
        lruCache.insertKeyValuePair('a', 9001)
        lruCache.getValueFromKey('a')
        lruCache.insertKeyValuePair('b', 2)
        lruCache.getValueFromKey('a')
        lruCache.getValueFromKey('b')
        lruCache.insertKeyValuePair('c', 3)
        lruCache.getValueFromKey('a')
        lruCache.getValueFromKey('b')
        lruCache.getValueFromKey('c')

    def test_case_3(self):
        lruCache = program.LRUCache(4)
        lruCache.insertKeyValuePair('a', 1)
        lruCache.insertKeyValuePair('b', 2)
        lruCache.insertKeyValuePair('c', 3)
        lruCache.insertKeyValuePair('d', 4)
        lruCache.getValueFromKey('a')
        lruCache.getValueFromKey('b')
        lruCache.getValueFromKey('c')
        lruCache.getValueFromKey('d')
        lruCache.insertKeyValuePair('e', 5)
        lruCache.insertKeyValuePair('d', 4)
        lruCache.getValueFromKey('a')
        lruCache.getValueFromKey('b')
        lruCache.getValueFromKey('c')
        lruCache.getValueFromKey('d')
        lruCache.getValueFromKey('e')

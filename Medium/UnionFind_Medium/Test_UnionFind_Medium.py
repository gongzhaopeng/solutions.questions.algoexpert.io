# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_UnionFind_Medium as program
import unittest

UnionFind = program.UnionFind


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        unionFind = UnionFind()
        self.assertTrue(unionFind.find(1) == None)
        unionFind.createSet(1)
        self.assertTrue(unionFind.find(1) == 1)
        unionFind.createSet(5)
        self.assertTrue(unionFind.find(1) == 1)
        self.assertTrue(unionFind.find(5) == 5)
        unionFind.union(5, 1)
        self.assertTrue(unionFind.find(5) == unionFind.find(1))

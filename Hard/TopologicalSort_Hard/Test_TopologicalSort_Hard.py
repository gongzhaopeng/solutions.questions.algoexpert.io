# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_TopologicalSort_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        jobs = [1, 2, 3, 4]
        deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)

    def test_case_2(self):
        jobs = [1, 2, 3, 4, 5, 6, 7, 8]
        deps = [
            [3, 1],
            [8, 1],
            [8, 7],
            [5, 7],
            [5, 2],
            [1, 4],
            [6, 7],
            [1, 2],
            [7, 6]
        ]
        order = program.topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), False)


def isValidTopologicalOrder(order, jobs, deps):
    visited = {}
    for candidate in order:
        for prereq, job in deps:
            if candidate == prereq and job in visited:
                return False
        visited[candidate] = True
    for job in jobs:
        if job not in visited:
            return False
    return len(order) == len(jobs)

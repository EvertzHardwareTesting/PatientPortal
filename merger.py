#!/usr/bin/env python

from robot.api import ExecutionResult, ResultVisitor


def merge(initial, *merged):
    result = ExecutionResult(initial)
    merger = Merger(result)
    for path in merged:
        merged = ExecutionResult(path)
        merger.merge(merged)
    result.save('merged.xml')


class Merger(ResultVisitor):

    def __init__(self, result):
        self.suite = result.suite
        self.current = None

    def merge(self, merged):
        merged.suite.visit(self)

    def start_suite(self, suite):
        if not self.current:
            self.current = self.suite
        else:
            self.current = self._find(self.current.suites, suite.name)

    def end_suite(self, suite):
        self.current = self.current.parent

    def visit_test(self, test):
        old = self._find(self.current.tests, test.name)
        index = self.current.tests.index(old)
        # need temporary list because self.current.tests[index] is not supported
        tests = list(self.current.tests)
        tests[index] = test
        self.current.tests = tests

    def _find(self, items, name):
        for item in items:
            if item.name == name:
                return item
        raise RuntimeError("Inconsistent structures.")


if __name__ == '__main__':
    import sys
    merge(*sys.argv[1:])

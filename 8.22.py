#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 10/12/2018.


import types


class Node:
    pass


class NodeVisitor:
    def visit(self, node):
        stack = [node]

        last_result = None

        while stack:

            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))

                else:
                    last_result = stack.pop()

            except StopIteration:
                stack.pop()

        return last_result

    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))

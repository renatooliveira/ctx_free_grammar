# coding: utf-8

"""
A Simple context-free grammar implementation.
"""


class Terminal:

    def __init__(self, symbol):
        self._symbol = symbol

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, sym):
        if sym.islower():
            self._symbol = sym
        else:
            raise ValueError("Terminals are meant to be lower cased.")

    def __unicode__(self):
        return self._symbol


class Variable:

    def __init__(self, symbol):
        self._symbol = symbol

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, sym):
        if sym.isupper():
            self._symbol = sym
        else:
            raise ValueError("Variables are meant to be upper cased.")

    def __unicode__(self):
        return self._symbol


class Rule:

    def __init__(self, variable, chain):
        self._variable = variable
        self.chains = chain

    @property
    def variable(self):
        return self._variable

    @variable.setter
    def variable(self, v):
        if isinstance(v, Variable):
            self._variable = v
        else:
            raise ValueError('It must be a variable.')

    def leftmost_derivation(self):
        pass

    def rightmost_derivation(self):
        pass


class Grammar:

    def __init__(self, rules, variables, terminals, e):
        self.rules = rules
        self.variables = variables
        self.terminals = terminals
        self.e = e

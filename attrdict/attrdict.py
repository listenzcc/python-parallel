"""
File: attrdict.py
Author: Chuncheng Zhang
Date: 2024-04-11
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Useful dictionary with attributes.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-04-11 ------------------------
# Requirements and constants
from typing import Any
import unittest


# %% ---- 2024-04-11 ------------------------
# Function and class

class AttrDict(dict):
    def __setattr__(self, name: str, value: Any) -> None:
        return super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        try:
            # Get the supposed-to-be attribute
            return super().__getattribute__(name)
        except AttributeError as e:
            # If not exists, search for key-value pairs
            if name not in self:
                raise AttributeError(
                    f'Attribute "{name}" does not exist') from e
            return super().get(name)


class TestMethods(unittest.TestCase):
    obj = None

    def __init__(self, obj: Any):
        super(TestMethods, self).__init__()
        self.obj = obj

    def runTest(self):
        self.check_is()
        self.check_raise()

    def check_is(self):
        print('Checking: check_is')
        for k in self.obj:
            self.assertIs(self.obj[k], eval(f'self.obj.{k}'))
            print(f'Passed key-value check: {k}')
        print(f'Passed: check_is')

    def check_raise(self):
        print('Checking: check_raise')
        with self.assertRaises(AttributeError):
            self.obj.not_exist
            print(f'Passed attributeError')
        with self.assertRaises(KeyError):
            self.obj['not_exist']
            print(f'Passed keyError')
        print(f'Passed: check_raise')


# %% ---- 2024-04-11 ------------------------
# Play ground
if __name__ == '__main__':
    ad = AttrDict(a=1, b=2)
    suite = unittest.TestSuite()
    suite.addTest(TestMethods(ad))
    unittest.TextTestRunner(verbosity=2).run(suite)


# %% ---- 2024-04-11 ------------------------
# Pending


# %% ---- 2024-04-11 ------------------------
# Pending

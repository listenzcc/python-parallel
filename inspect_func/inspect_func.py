"""
File: inspect_func.py
Author: Chuncheng Zhang
Date: 2024-04-12
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Inspect the function/method, parse out its arguments.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-04-12 ------------------------
# Requirements and constants
import inspect


# %% ---- 2024-04-12 ------------------------
# Function and class
def fun_1(b, a, c=1, d='default', **kwargs):
    '''Example function 1'''
    return


def inspect_func(func):
    '''Inspect the function'''
    signature = inspect.signature(func)

    all_args = [
        (v.name, v.default, v.kind)
        for v in signature.parameters.values()
    ]

    positional_args = [
        v.name
        for v in signature.parameters.values()
        if v.default is inspect.Parameter.empty
    ]

    default_args = [
        (v.name, v.default)
        for v in signature.parameters.values()
        if v.default is not inspect.Parameter.empty
    ]

    return signature, positional_args, default_args, all_args


# %% ---- 2024-04-12 ------------------------
# Play ground
if __name__ == '__main__':
    signature, positional_args, default_args, all_args = inspect_func(fun_1)
    print(f'Parsed function signature: {signature}')
    print(f'positional_args:\t{positional_args}')
    print(f'default_args:\t{default_args}')
    print(f'all_args:')
    for arg in all_args:
        print(f'\t{arg}')


# %% ---- 2024-04-12 ------------------------
# Pending


# %% ---- 2024-04-12 ------------------------
# Pending

# %%

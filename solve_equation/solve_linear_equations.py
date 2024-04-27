"""
File: solve_linear_equations.py
Author: Chuncheng Zhang
Date: 2024-04-22
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Amazing things

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-04-22 ------------------------
# Requirements and constants

# importing library sympy
from sympy import symbols, Eq, solve


# %% ---- 2024-04-22 ------------------------
# Function and class
def solve_equations(eq1: list, eq2: list):
    print('-' * 80)
    # defining symbols used in equations
    # or unknown variables
    x, y = symbols('x,y')

    # defining equations
    eq1 = Eq((eq1[0]*x+eq1[1]*y), eq1[2])
    eq2 = Eq((eq2[0]*x+eq2[1]*y), eq2[2])
    print("Equations:")
    print(eq1)
    print(eq2)

    # solving the equation
    return solve((eq1, eq2), (x, y)), x, y


# print(solve_equations([1, 1, 1], [1, -1, 1]))
for d in [11880, 43080, 73080, 145080, 250080]:
    ans, x, y = solve_equations([1, 1, 7.465], [1080, d, 9937])
    print(ans)
    print(ans[y] * 1e2)

# %%

# %%

# %% ---- 2024-04-22 ------------------------
# Play ground
# defining symbols used in equations
# or unknown variables
x, y = symbols('x,y')

# defining equations
eq1 = Eq((x+y), 1)
print("Equation 1:")
print(eq1)
eq2 = Eq((x-y), 1)
print("Equation 2")
print(eq2)

# solving the equation
print("Values of 2 unknown variable are as follows:")
print(solve((eq1, eq2), (x, y)))


# %% ---- 2024-04-22 ------------------------
# Pending


# %% ---- 2024-04-22 ------------------------
# Pending

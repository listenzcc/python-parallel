"""
File: pillow-image-overlap.py
Author: Chuncheng Zhang
Date: 2024-04-27
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


# %% ---- 2024-04-27 ------------------------
# Requirements and constants
import numpy as np

from PIL import Image, ImageDraw
from pathlib import Path

root = Path(__file__).parent


# %% ---- 2024-04-27 ------------------------
# Function and class

img = Image.open(root.joinpath('raw.jpg'))

# (height, width)
size = img.size

background = Image.fromarray(
    np.zeros((size[1], size[0], 3), dtype=np.uint8)).convert('RGB')

alpha_mask = np.zeros((size[1], size[0]), dtype=np.uint8)
alpha_mask[100:500, 100:800] = 255
alpha_mask = Image.fromarray(alpha_mask, mode='L')

background.paste(img, (500, 500), alpha_mask)
background

# %%


# %% ---- 2024-04-27 ------------------------
# Play ground


# %% ---- 2024-04-27 ------------------------
# Pending


# %% ---- 2024-04-27 ------------------------
# Pending

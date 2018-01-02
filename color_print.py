# !python3
# coding: utf-8
from __future__ import print_function
import time
import random

mystr = "this is a colorful message."

raw_color = [i for i in range(30, 38)]
color_choice = "\033[1;{0}m {1} \033[0m"

def color_str(msg):
    for char in msg:
        print(color_choice.format(random.choice(raw_color), char), end="\n", flush=True)
        time.sleep(0.3)

color_str(mystr)

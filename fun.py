# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:25:39 2019

@author: user
"""

import random


def guess(l, r):
    return random.randint(l, r)


l, r = map(int, input("Enter Two Number (range): ").split())
print("Random Number is between ", l, "and ", r, "is : ", guess(l, r))

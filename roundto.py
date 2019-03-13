# -*- coding: utf-8 -*-
"""
Function for rounding a number to a nice number
Intended for use on the maximum value of a dataset for determining the axis range
Emily Saurette
March 11, 2019
"""
import numpy as np

# should be evenly divisible by the amount of ticks - 1 because the first tick is forced to zero
# should nice numbers also be even numbers?

def round_to_factor_of(x,y):
    '''takes a number, x, increases it by 10%, and returns the next highest number that is a factor of y-1'''
    x *= 1.1
    if x % y-1 == 0:
        return x
    else:
        return np.ceil(x/(y-1))*(y-1)

def nice_numbers(x,y):
    '''calls round_to_factor_of takes the number it returns and returns a nice looking value that is larger than it'''
    r = round_to_factor_of(x,y)
    if r <= 7:
        return x
    elif 7 < r <= 20:
        return r
    elif 20 < r < 1000:
        return np.round(r/100, 1)*100
    elif r >= 1000:
        return np.round(r/1000, 1)*1000
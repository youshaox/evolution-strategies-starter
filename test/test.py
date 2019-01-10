#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by youshaox on 3/1/19
"""
function:

"""
import sys

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

temp = Celsius(32)
temp.temperature = 33
print(temp.temperature)
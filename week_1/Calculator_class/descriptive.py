#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""

import math
class Calculator:
    def __init__(self, data):
        self.data = data
        self.data.sort()
        self.length = len(data)
        self.mean = sum(data)/len(data)
        if self.length % 2 == 0:
            self.median = (data[int(self.length/2)-1]+data[int(self.length/2)]) / 2
        else:
            self.median = (data[int((self.length+1)/2)-1])
        difference_sq = [(x - self.mean)**2 for x in data]
        self.variance = sum(difference_sq)/(self.length-1)
        self.stand_dev = math.sqrt(self.variance)
    def add_data(self, new_data):
        if type(new_data) == list:
            self.data.extend(new_data)
        else:
            self.data.append(new_data)
        self.__init__(self.data)
        


    def remove_data(self, new_data2):
        for x in new_data2:
            for y in self.data:
                if y != x:
                    continue
                elif y == x:
                    self.data.remove(x)
        self.__init__(self.data)
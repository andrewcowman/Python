# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:35:52 2016

@author: Andrew
"""

class Normalize(object):
    def __init__(self):
        self.header = []
        self.column_map = {}
        
    def load_csv(self, file):
        result = []
        first = True
        
        with open(file, 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    if first:
                        first = False
                        self.header = row
                    else:
                        result.append(row)
                        
        for idx in range(0, len(self.header)):
            self.column_map[self.header[idx]] = idx
            
        return result
        
    def normalize_col(self, data, col, norm_low, norm_high):
        data_low = self.find_low(data, col)
        data_high = self.find_high(data, col)
        
        for row in data:
            row[col] = ((row[col] - data_low) / (data_high - data_low)) * (norm_high - norm_low) + norm_low
        
    def find_low(self, data, col):
        min_val = sys.float_info.max
        for row in data:
            min_val = min(min_val, row[col])
        return min_val
        
    def find_high(self, data, col):
        max_val = sys.float_info.min
        for row in data:
            max_val = max(max_val, row[col])
        return max_val
        
    def enumerate_classes(self, data, col):
        species = {}
        idx = 0
        for row in data:
            key = row[col]
            if key not in species:
                species[key] = idx
                idx += 1
        return species
        
    def norm_one_of_n(self, data, col, species, norm_low, norm_high):
        for row in data:
            key = row[col]
            value = species[key]
            row.pop(col)
            for i in range(0, len(species)):
                if i == value:
                    row.insert(col + i, norm_high)
                else:
                    row.insert(col + i, norm_low)
                    
    def numerate(self, data, col):
        for row in data:
            row[col] = float(row[col])


import csv
import os
import sys

irisFile = os.path.relpath("datasets/iris.csv")

norm = Normalize()
data = norm.load_csv(irisFile)

for i in range(0, 4):
    norm.numerate(data, i)
    norm.normalize_col(data, i, -1, 1)
    
species = norm.enumerate_classes(data, 4)
norm.norm_one_of_n(data, 4, species, -1, 1)

for row in data:
    print(row)
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:09:54 2016

@author: Andrew
"""

import os
import csv
from scipy.cluster.vq import *
import numpy as npy

class Normalize(object):
    def __init__(self):
        self.headers = []
        self.column_map = {}
        
    def load_csv(self, file):
        data = []
        first = True
        
        with open(file, 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    if first:
                        self.headers = row
                        first = False
                    else:
                        data.append(row)
                        
        for i in range(0, len(self.headers)):
            self.column_map[self.headers[i]] = i
            
        return data
        
    def numerate(self, data, col):
        for row in data:
            row[col] = float(row[col])
            
    def extract_column(self, data, col):
        result = []
        for row in data:
            result.append(row[col])
            
        return result
        
    def delete_column(self, data, col):
        for row in data:
            del row[col]
    
    
    
file = os.path.relpath("datasets/iris.csv")
norm = Normalize()

data = norm.load_csv(file)

species = norm.extract_column(data, 4)
norm.delete_column(data, 4)

for i in range(0, 4):
    norm.numerate(data, i)
    
clusters = 3
res, idx = kmeans2(npy.array(data), clusters)

for cluster in range(0, clusters):
    print("Cluster #" + str(cluster + 1))
    for i in range(0, len(idx)):
        if idx[i] == cluster:
            print(str(data[i]) + ", " + species[i])

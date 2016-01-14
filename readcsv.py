# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:29:03 2016

@author: Andrew
"""

import csv
import os

file = os.path.relpath("datasets/iris.csv")

with open(file, 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
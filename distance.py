# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:37:40 2016

@author: Andrew
"""

import sys
import os
from scipy.spatial import distance

pos1 = [4.0, 10.0, 9.0]
pos2 = [11.0, 2.0, 7.0]
pos3 = [12.0, 9.0, 7.0]

print("pos1 -> pos2: " + str(distance.euclidean(pos1, pos2)))
print("pos1 -> pos3: " + str(distance.euclidean(pos1, pos3)))
print("pos3 -> pos2: " + str(distance.euclidean(pos3, pos2)))
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:29:23 2021

@author: Tran Cuong
K-MEANS CLUSTERING
"""

#%% INTRODUCTION

"""
About this lab:
    - There are many models for clustering out there. 
    - In this lab, we will be presenting the model that is considered the one of the simplest model among them.
    - Despite its simplicity, k-means is vastly used for clustering in many data science applications.
    - Especially, k-means is useful if you nead to quickly discover insights from unlabeled data

Some real-world application of k-means include:
    - Customer segmentation
    - Understand what the visitors of a website are trying to accomplish
    - Pattern recognition
    - Data compression
    
In this lab, we will learn k-means clustering with 3 examples:
    1. k-means on a randomly generated dataset
    2. using k-means for customer segmentation
"""

#%% LIBRARIES

import random #library for random number generation
import numpy #library for vectorized computation
import pandas as pd #library to process data as dataframes

import matplotlib.pyplot as plt #plotting library

from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

print('Libraries imported')

#%% K-MEANS ON A RANDOMLY GENERATED DATASET

# let's demonstrate how k-means works with an example of engineered data points
# 30 data points belonging to 2 different clusters (x1 and x2)

# data
x1 = [-4.9, -3.5, 0, -4.5, -3, -1, -1.2, -4.5, -1.5, -4.5, -1, -2, -2.5, -2, -1.5, 4, 1.8, 2, 2.5, 3, 4, 2.25, 1, 0, 1, 2.5, 5, 2.8, 2, 2]
x2 = [-3.5, -4, -3.5, -3, -2.9, -3, -2.6, -2.1, 0, -0.5, -0.8, -0.8, -1.5, -1.75, -1.75, 0, 0.8, 0.9, 1, 1, 1, 1.75, 2, 2.5, 2.5, 2.5, 2.5, 3, 6, 6.5]

print('Datapoints defined!')

# Define a function that assigns each datapoint to a cluster
colors_map = np.array(['b', 'r'])
def assign_members(x1, x2, centers):
    compare_to_first_center = np.sqrt()

























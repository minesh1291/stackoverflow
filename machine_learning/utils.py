import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calculate_kn_distance(X, k):
    """
    First you can define a function to calculate the distance of each point to its k-th nearest neighbor:
    Then, once you have defined your function, you can choose a k value and plot the histogram to find a knee to define an appropriate epsilon value.
    Find optimal eps for DBSCAN Clustering
    
    Usage:
      eps_dist = calculate_kn_distance(X, 2)
      plt.hist(eps_dist, bins=60)
      plt.ylabel('n');
      plt.xlabel('Epsilon distance');
    """
    kn_distance = []
    for i in range(len(X)):
        eucl_dist = []
        for j in range(len(X)):
            eucl_dist.append(
                math.sqrt(
                    ((X[i,0] - X[j,0]) ** 2) +
                    ((X[i,1] - X[j,1]) ** 2)))

        eucl_dist.sort()
        kn_distance.append(eucl_dist[k])

    return kn_distance


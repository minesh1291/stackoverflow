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


def transfrom_all_data(transformer, train, test, feature_list):
    """
    Apply transformer to train and test features
    """
    train_trans = transformer.fit_transform(train[feature_list])
    test_trans = transformer.transform(test[feature_list])
    
    if type(train_trans) != np.ndarray:
        train_trans = np.array(train_trans)
        test_trans = np.array(test_trans)
    
    return train_trans, test_trans


def make_features(transformer, train, test, feature_list, name, normalize=False, scaler=None):
    """
    Add newly generated transformed features to train and test dataframe
    
    Usage:
        scaler = StandardScaler()
        logTrans = FunctionTransformer(np.log1p)
        train_X, val_X = make_features(qTrans, train_X, val_X, feature_list=range(10), name="qTrans", normalize=False, scaler=scaler)
    """
    train, test = train.copy(), test.copy()
    train_trans, test_trans = transfrom_all_data(transformer, train, test, feature_list)
    
    if normalize and scaler is not None:
        train_trans = scaler.fit_transform(train_trans).astype(np.float32)
        test_trans = scaler.transform(test_trans).astype(np.float32)
    
    for i in range(train_trans.shape[1]):
        train['{0}_{1}'.format(name, i)] = train_trans[:, i]
        test['{0}_{1}'.format(name, i)] = test_trans[:, i]
        
    return train, test


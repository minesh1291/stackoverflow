import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors

import math
from kneebow.rotor import Rotor


""" Transform """

def transfrom_all_data(transformer, train, test, feature_list):
    """
    Apply transformer to train and test features
    
    Usage:
        logTrans = FunctionTransformer(np.log1p)
        train_trans, test_trans = transfrom_all_data(transformer, train, test, feature_list)
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


""" Optimal Parameters """

def calculate_kn_distance(X, neigh=2):
    neigh = NearestNeighbors(n_neighbors=neigh)
    nbrs = neigh.fit(X)
    distances, indices = nbrs.kneighbors(X)
    return distances[:,1:].reshape(-1,1)


def get_eps(X, neigh=2):
    eps_dist = np.sort(calculate_kn_distance(X, neigh=neigh))
    plt.hist(eps_dist, bins=60)
    plt.ylabel('n');
    plt.xlabel('Epsilon distance');
    plt.show()
    
    rotor = Rotor()
    curve_xy = np.concatenate([np.arange(eps_dist.shape[0]).reshape(-1, 1), eps_dist],1)
    rotor.fit_rotate(curve_xy)
    rotor.plot_elbow()
    e_idx = rotor.get_elbow_index()
    
    return curve_xy[e_idx]


def calc_optimal_components(X, var_thr=0.95):
    """
    Find optimal numbers of PCA components
    
    Usage:
        calc_optimal_components(X)
    """
    
    pca = PCA(min(X.shape))
    pca.fit(X)

    var_ratio_cum = pca.explained_variance_ratio_.cumsum()
    n_comp = np.where(var_ratio_cum>=var_thr)[0][0]

    plt.plot(range(min(X.shape)), var_ratio_cum, "o-")
    plt.vlines([n_comp], ymin=var_ratio_cum[0], ymax=var_ratio_cum[n_comp], linestyles="--", color="red", alpha=0.5)
    plt.plot([n_comp], var_ratio_cum[n_comp], marker="x", markersize=12)
    
    print("n_components: ", n_comp)
    return n_comp

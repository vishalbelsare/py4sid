from __future__ import division
import numpy as np
from numpy.random import rand, randn

def rand_lds(n,p,eig_min=0.5,eig_max=1.0):
    eignorms = eig_min + (eig_max-eig_min)*rand(n)
    temp = randn(n,n)
    eigvals, T = np.linalg.eig(randn(n,n))
    eigvals *= eignorms / np.abs(eigvals)

    A = np.real(T.dot(np.diag(eigvals)).dot(np.linalg.inv(T)))
    B = np.eye(n)
    C = np.vstack((np.eye(n),np.zeros((p-n,n))))
    D = 0.01*np.eye(p)

    return A,B,C,D

def rand_data(T,(A,B,C,D)):
    p,n = C.shape
    x = np.empty((T,n))

    v = randn(T,n)
    x[0] = 0
    for t in xrange(T-1):
        x[t+1] = A.dot(x[t]) + B.dot(v[t])

    w = randn(T,p)
    y = C.dot(x.T).T + D.dot(w.T).T

    return x, y

def rand_lds_and_data(T,n,p):
    lds = rand_lds(n,p)
    data = rand_data(T,lds)
    return lds, data



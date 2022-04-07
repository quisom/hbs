import os
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
plt.rcParams['pgf.texsystem']= 'pdflatex'

def s_MFN_day(L, n):
    return n*L/(2**L-1)*86400*250/1024**2

def d_MFN(L, n):
    return n*L**2/(2**L-1) + L

def plot_optimal_L():
    n_range = range(100, 50000, 100)
    res = [optimize.minimize(d_MFN, 10, args = [n])\
        for n in n_range]
    suc = [(r['success']) for r in res]
    if all(suc):
        print('OK!')

    L_argmin = [L['x'][0] for L in res]
    s_mfn = [s_MFN_day(L, n) for L, n in zip(L_argmin, n_range)]

    fig, ax = plt.subplots(2, 1)    
    ax[0].plot(n_range, L_argmin, label =\
        '$\mathrm{argmin}(d_{MNF}(L, n))$', linestyle = '-')
    ax[1].plot(n_range, s_mfn, label = '$s_{MNF}(day)$'\
        , linestyle = '-')
    ax[0].legend()
    ax[1].legend()
    ax[1].set_xlabel('n')
    ax[0].set_ylabel('L')
    ax[1].set_ylabel('MB')
    os.makedirs('pics', exist_ok = True)
    plt.savefig('pics/optimal_L_mfn.pgf')
    plt.show()

if __name__ == "__main__":
    plot_optimal_L()

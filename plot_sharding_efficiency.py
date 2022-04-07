import os
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['pgf.texsystem'] = 'pdflatex'

def ratio_blocks_mfn_vs_full(N, L):
    return N*L**2/(2**L-1)**2 + L/(2**L-1)

def plot_sharding_efficiency():
    n_trans = 4200
    L = 25
    x = range(1, L)

    y1 = [np.log10(ratio_blocks_mfn_vs_full(n_trans,i)) for i in x]
    y2 = [np.log10(ratio_blocks_mfn_vs_full(2**i-1,i)) for i in x]
    y3 = [np.log10((2**i-1)/600) for i in x]

    fig, ax = plt.subplots()    
    ax.axhline(y = 0, color = 'k', linewidth = 1)
    ax.plot(x, y1, label = '$\lg(r), N = 4200$', linestyle = '-')
    ax.plot(x, y2, label = '$\lg(r), N = 2^L-1$', linestyle = '--')
    ax.plot(x, y3, label = '$\lg((2^L-1)/600)$', linestyle = '-.')
    ax.legend()
    plt.xlabel('L')
    os.makedirs('pics', exist_ok = True)
    plt.savefig('pics/sharding_efficiency.pgf')
    plt.show()

if __name__ == "__main__":
    plot_sharding_efficiency()

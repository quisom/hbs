import os
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['pgf.texsystem'] = 'pdflatex'

def d_MFN_day(L, n):
    return (n*L**2/(2**L-1) + L)*86400*250/1024**2

def plot_download_mfn():
    n_1 = 1700
    n_2 = 10000
    n_3 = 50000
    L = 30
    x = range(1, L)

    y1 = [np.log10(d_MFN_day(i, n_1)) for i in x]
    y2 = [np.log10(d_MFN_day(i, n_2)) for i in x]
    y3 = [np.log10(d_MFN_day(i, n_3)) for i in x]

    fig, ax = plt.subplots()
    ax.plot(x, y1, label = f'$\lg(d_{{MFN}}(day)), n = {n_1}$',\
        linestyle = '-')
    ax.plot(x, y2, label = f'$\lg(d_{{MFN}}(day)), n = {n_2}$',\
        linestyle = '--')
    ax.plot(x, y3, label = f'$\lg(d_{{MFN}}(day)), n = {n_3}$',\
        linestyle = '-.')
    ax.legend()
    plt.xlabel('L')
    plt.ylabel('$\lg(\mathrm{MB})$')
    os.makedirs('pics', exist_ok = True)
    plt.savefig('pics/download_mfn.pgf')
    plt.show()

if __name__ == "__main__":
    plot_download_mfn()

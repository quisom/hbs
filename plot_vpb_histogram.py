import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['pgf.texsystem']= 'pdflatex'

def plot_vpb_hist():
    T = pd.read_hdf('data/transactions.h5', 'tx_df')
    T = T[T['output_value'] > 0]
    vpb = T['output_value']/(8*T['size'])

    count, bins, ignored = plt.hist(np.log10(vpb),\
    bins = 100, density = True)

    mu = np.sum(np.log10(vpb))/len(vpb)
    sigma = np.sqrt(np.sum((np.log10(vpb) - mu)**2)/(len(vpb)-1))

    x = np.linspace(min(bins), max(bins), 100)
    pdf = (np.exp(-(x - mu)**2 / (2 * sigma**2))
    / (sigma * np.sqrt(2 * np.pi)))
    plt.plot(x, pdf, linewidth = 1.5, color = 'r')
    plt.xlabel(r'$\lg(\beta(t))$')
    plt.ylabel('density')
    os.makedirs('pics', exist_ok = True)
    plt.savefig('pics/tx_vpb.pgf')
    plt.show()
    
if __name__ == "__main__":
    plot_vpb_hist()

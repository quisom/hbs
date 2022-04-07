import numpy as np
import pandas as pd

def segment_transactions(L, T, key):
    T = T.sort_values(ascending = False, by = key)

    M = T[key].values[0]
    m = T[key].values[-1]

    S_L = (np.log10(M)-np.log10(m))/L
    #S_L = (np.ceil(np.log10(M))-np.floor(np.log10(m)))/L

    indx = [0]*(L+1)
    indx[0] = 0
    s = T[key]
    C = np.log10(M) - S_L; l = 0
    for r, v in enumerate(s):
        if np.log10(v) < C:
            l = l+1
            indx[l] = r
            C = C - S_L
    indx[L] = len(s)
    Ts = []
    for l in range(L):
        Ts.append(T[indx[l]:indx[l+1]])
    return Ts
if __name__ == "__main__":
    tx_df = pd.read_hdf('data/transactions.h5', 'tx_df')
    tx_df.reset_index(drop = True, inplace = True)
    tx_df = tx_df[tx_df['output_value'] > 0]
    tx_df['vpb'] = tx_df['output_value']/(8*tx_df['size'])
    Ts = segment_transactions(6, tx_df, 'vpb')

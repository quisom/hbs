import numpy as np
import pandas as pd
from segment_transactions import *
np.set_printoptions(precision = 2)

def compute_c_eta_and_eta(Ts, num_blocks = 493):
    s = 0
    for l in range(len(Ts)):
        s += Ts[l]['vpb'].mean()*8*Ts[l]['size'].sum()
    c_eta = 600*num_blocks*10**8/s
    eta = []
    for l in range(len(Ts)):
        eta.append(c_eta*Ts[l]['vpb'].mean()/10**8) 
    return c_eta, eta

def compute_time_per_level(eta, Ts, num_blocks = 493):
    t = []
    for l in range(len(Ts)):
        t.append(eta[l]*8*Ts[l]['size'].sum()/num_blocks)
    return t

if __name__ == "__main__":
    tx_df = pd.read_hdf('data/transactions.h5', 'tx_df')
    tx_df.reset_index(drop = True, inplace = True)
    tx_df = tx_df[tx_df['output_value'] > 0]
    tx_df['vpb'] = tx_df['output_value']/(8*tx_df['size'])
    Ts = segment_transactions(6, tx_df, 'vpb')

    num_blocks = tx_df['block_height'].nunique()
    c_eta, eta = compute_c_eta_and_eta(Ts, num_blocks)
    print(f'c_eta = {c_eta:.2}')
    print('eta =' , np.array(eta))
    times = compute_time_per_level(eta, Ts, num_blocks)
    print('times =', np.array(times))
    
    

import numpy as np
import pandas as pd
from segment_transactions import *
from compute_c_and_tis import *

def generate_latex_table_2(eta, t_level, Ts):
    text = """\def\\arraystretch{1.1}
\\begin{table}
\\begin{tabular}{|"""
    text += 'c|'*(len(Ts)+1)+"""}
\hline
$l$"""
    for i in range(len(Ts)):
        text += f' & {i}'
    text +="\\\ \hhline{|"
    text += '=|'*(len(Ts)+1)+"""}
$|\mathcal{T}_l|$""" 
    for i in range(len(Ts)):
        text += f' & {len(Ts[i])}'
    text += """ \\\ \hline
$\overline{\\bsize(\mathcal{T}_l)}$""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["size"].mean():.3}'
    text += """ \\\ \hline
min($\\beta(t)$)""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["vpb"].min():.3}'
    text += """ \\\ \hline
max($\\beta(t)$)""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["vpb"].max():.3}'
    text += """ \\\ \hline
$\overline{\\beta(t)}$""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["vpb"].mean():.3}'
    text += """ \\\ \hline
min($v(t)$)""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["output_value"].min():.3}'
    text += """ \\\ \hline
max($v(t)$)""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["output_value"].max():.3}'
    text += """ \\\ \hline
$\overline{v(t)}$""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["output_value"].mean():.3}'
    text += """ \\\ \hline
$\sum v(t)$""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["output_value"].sum():.3}'
    text += """ \\\ \hline
$\\ti_l$""" 
    for i in range(len(Ts)):
        text += f' & {eta[i]:.3}'
    text += """ \\\ \hline
$t_l$""" 
    for i in range(len(Ts)):
        text += f' & {t_level[i]:.3}'
    text += """ \\\ \hline    
\end{tabular}
\caption{Distribution of transaction values after segmentation: $L=2$}
\label{table:segmented_txs_L_2}
\end{table}"""
    return text

if __name__ == "__main__":
    tx_df = pd.read_hdf('data/transactions.h5', 'tx_df')
    tx_df.reset_index(drop = True, inplace = True)
    tx_df = tx_df[tx_df['output_value'] > 0]
    tx_df['vpb'] = tx_df['output_value']/(8*tx_df['size'])
    Ts = segment_transactions(2, tx_df, 'vpb')
    num_blocks = tx_df['block_height'].nunique()
    c_eta, eta = compute_c_eta_and_eta(Ts, num_blocks)
    times = compute_time_per_level(eta, Ts, num_blocks)
    text = generate_latex_table_2(eta, times, Ts)
    print(text)

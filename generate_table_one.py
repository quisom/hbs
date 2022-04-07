import numpy as np
import pandas as pd
from segment_transactions import *

def generate_latex_table(Ts):
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
min($\\beta(t)$)""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["vpb"].min():.2}'
    text += """ \\\ \hline
max($\\beta(t)$)""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["vpb"].max():.2}'
    text += """ \\\ \hline
$\overline{\\beta(t)}$""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["vpb"].mean():.2}'
    text += """ \\\ \hline
min($v(t)$)""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["output_value"].min():.2}'
    text += """ \\\ \hline
max($v(t)$)""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["output_value"].max():.2}'
    text += """ \\\ \hline
$\overline{v(t)}$""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["output_value"].mean():.2}'
    text += """ \\\ \hline
$\sum v(t)$""" 
    for i in range(len(Ts)):
        text += f' & {Ts[i]["output_value"].sum():.2}'
    text += """ \\\ \hline
\end{tabular}
\caption{...}
\label{...}
\end{table}"""
    return text
if __name__ == "__main__":
    tx_df = pd.read_hdf('data/transactions.h5', 'tx_df')
    tx_df.reset_index(drop = True, inplace = True)
    tx_df = tx_df[tx_df['output_value'] > 0]
    tx_df['vpb'] = tx_df['output_value']/(8*tx_df['size'])
    Ts = segment_transactions(6, tx_df, 'vpb')
    text = generate_latex_table(Ts)
    print(text)

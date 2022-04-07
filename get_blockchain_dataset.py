import os
import sys
from blockchain_parser.blockchain import Blockchain
import random
import pandas as pd

def get_blockchain_data(blockchain_dir):
    columns_blk = ['block_height', 'block_hash', 'version',\
        'previous_block_hash', 'merkle_root', 'timestamp',\
        'bits', 'nonce', 'difficulty']
    types_blk = ['uint32', 'str', 'uint32', 'str', 'str',\
        'uint32', 'uint32', 'uint32', 'float']
    dtypes_blk = {c: t for (c, t) in zip(columns_blk, types_blk)}
    columns_tx = ['block_height', 'txid', 'hash', 'version', 'n_inputs',\
        'n_outputs', 'is_segwit', 'is_coinbase', 'size', 'output_value']
    types_tx = ['uint32', 'str', 'str', 'uint32', 'uint32',\
    'uint32', 'bool', 'bool', 'uint32', 'uint64']
    dtypes_tx = {c: t for (c, t) in zip(columns_tx, types_tx)}
    blk_df = pd.DataFrame(columns = columns_blk)
    blk_df = blk_df.astype(dtype = dtypes_blk)
    tx_df = pd.DataFrame(columns = columns_tx)
    tx_df = tx_df.astype(dtype = dtypes_tx)

    blockchain = Blockchain(os.path.expanduser(f'{blockchain_dir}/btc/blocks'))
    bx_list = []
    for blk in blockchain.get_ordered_blocks(\
        os.path.expanduser(f'{blockchain_dir}/btc/blocks/index'),\
        start = 650000, end = 700000):
        if (random.random() > 0.01):
            continue
        h = blk.header
        df = pd.DataFrame([[blk.height, blk.hash, h.version,\
        h.previous_block_hash, h.merkle_root, h.timestamp,\
        h.bits, h.nonce, h.difficulty]], columns = columns_blk)
        blk_df = blk_df.append(df)
        tx_list = []
        for tx in blk.transactions:
            sum_out = 0
            for tout in tx.outputs:
                sum_out = sum_out + tout.value
            tx_list.append([blk.height, tx.txid, tx.hash, tx.version,\
            tx.n_inputs, tx.n_outputs, tx.is_segwit, tx.is_coinbase(),\
            tx.size, sum_out])
    tx_df = tx_df.append(pd.DataFrame(tx_list, columns = columns_tx))

    tx_df.reset_index(drop = True, inplace = True)
    blk_df.reset_index(drop = True, inplace = True)
    os.makedirs('data', exist_ok = True)
    tx_df.to_hdf('data/transactions.h5', key='tx_df', mode='w')
    blk_df.to_hdf('data/transactions.h5', key='blk_df')
    
if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print('No directory {blockchain_dir}/btc/blocks supplied as an argument!')
    else:
        print(f'{sys.argv[1]}/btc/blocks')
        get_blockchain_data(sys.argv[1])
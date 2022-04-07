import hashlib
import os

def shardf(l, string):
    b = hashlib.sha256(bytes(string, 'utf-8')).digest()
    shifts = []
    for r in range(l//8+1):
        shifts = shifts + [int(i) for i in f'{b[r]:08b}']
    shards = [0]*(l+1)
    for i in range(l):
        if shifts[i] == 0:
            shards[i+1] = 2*shards[i]
        else:
            shards[i+1] = 2*shards[i]+1
    return shards[l], shards

def pdf_is_uniform_in_s(n = 100000):
    c = 0
    for i in range(n):
        s_l, s = shardf(5, str(os.urandom(128)))
        if(s[5] <= 1):
            c += 1
    print(f'{c} of {2/32*n} expected')

if __name__ == "__main__":
    s_l, s = shardf(10, 'shard_me')
    print(f's = {s}')
    pdf_is_uniform_in_s(100000)

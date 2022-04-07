import hashlib
import time
import os
import matplotlib.pyplot as plt
plt.rcParams['pgf.texsystem']= 'pdflatex'

def plot_hashing_time():
    n = 100
    x = range(n)
    y = []
    for i in x:
        m = os.urandom(i*1024**2)
        time_b = time.time()
        hashlib.sha256(m).hexdigest()
        time_e = time.time()
        y.append(time_e - time_b)

    fig = plt.subplots()    
    plt.plot(x,y)
    plt.xlabel("size[MB]")
    plt.ylabel("time[s]")
    os.makedirs('pics', exist_ok = True)
    plt.savefig('pics/hash_time.pgf')
    plt.show()

if __name__ == "__main__":
    plot_hashing_time()


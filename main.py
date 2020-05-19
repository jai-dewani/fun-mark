import time as t
from random import randint
import numpy as np
import matplotlib.pyplot as plt


class Benchmark:

    def __init__(self):
        self.time = []
        self.memory = []

    def run(self, func, data):
        start = t.time()
        func(data)
        end = t.time()
        runtime = end - start
        print(f'The runtime for {func.__name__} took {runtime} seconds to complete')
        return runtime

    def add(self, index, time=None, memory=None):
        self.time.append([index, time])
        self.memory.append([index, memory])
    
    def plot(self, xlabel="", ylabel="", title=""):
        time = np.array(self.time)
        print(time)
        print(time[:,0])
        print(time[:,1])
        plt.plot(time[:,0],time[:,1])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

def s(ar):
    ar.sort()
    return ar

test = Benchmark()
for i in range(10,10**6,1000):
    ar = [randint(1,10**5) for i in range(i)]
    time = test.run(s,ar)
    test.add(len(ar),time)
test.plot()
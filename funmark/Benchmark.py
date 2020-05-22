import time as t
import numpy as np
import matplotlib.pyplot as plt
import tracemalloc

class Benchmark:

    def __init__(self):
        self.time = []
        self.memory = []
        self.plot = None
        self.functionName = None

    def run(self, func, *argv):
        self.functionName = func.__name__
        tracemalloc.start()
        start = t.time()
        # print(var)
        func(argv)
        end = t.time()
        __,peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        runtime = end - start
        print(f'The runtime for {func.__name__} took {runtime} seconds to complete')
        return runtime, peak/10**6

    def add(self, index, time=None, memory=None):
        if time:
            self.time.append([index, time])
        if memory:
            self.memory.append([index, memory])
    
    def plotGraph(self, xlabel="", ylabel="", title="", label="", show=True, plt=plt):
        time = np.array(self.time)
        plt.plot(time[:,0],time[:,1], label=label)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        if show:
            plt.show()
        return plt

    def compare(self, xlabel="", ylabel="", title="", *argv):
        temp = self.plotGraph(xlabel=xlabel, ylabel=ylabel, title=title, label=self.functionName, show=False, plt=plt)
        for other in argv:
            # time2 = np.array(other.time, plt=temp)
            # plt.plot(time2[:,0],time2[:,1])
            other.plotGraph(xlabel=xlabel, ylabel=ylabel, title=title, label=other.functionName, show=False, plt=temp)
        temp.legend(loc="upper right")
        temp.show()
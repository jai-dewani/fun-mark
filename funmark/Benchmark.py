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

    def run(self, func, *argv, logs=True):
        """
        return:
        runtime: int, the time it took to run (seconds)
        memory: int, total memeory took by the function (KB)
        """
        self.functionName = func.__name__
        tracemalloc.start()
        start = t.time()
        # print(var)
        func(argv)
        end = t.time()
        __,peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        runtime = end - start
        print(f'The runtime for {func.__name__} took {runtime} seconds to complete with {peak/10**3}KB memory')
        return runtime, peak/10**3

    def add(self, index, time=None, memory=None):
        if time!=None:
            self.time.append([index, time])
        if memory!=None:
            self.memory.append([index, memory])
    
    def plotTime(self, xlabel="", ylabel="", title="", label="", show=True, plt=plt):
        time = np.array(self.time)
        print('time',time)
        plt.plot(time[:,0],time[:,1], label=label)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        if show:
            plt.show()
        return plt

    def plotMemory(self, xlabel="", ylabel="", title="", label="", show=True, plt=plt):
        memory = np.array(self.memory)
        print('memory',memory)
        plt.plot(memory[:,0],memory[:,1], label=label)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        if show:
            plt.show()
        return plt

    def compareTime(self, xlabel="", ylabel="", title="", *argv):
        time_plt = self.plotTime(xlabel=xlabel, ylabel=ylabel, title=title, label=self.functionName, show=False, plt=plt)
        for other in argv:
            other.plotTime(xlabel=xlabel, ylabel=ylabel, title=title, label=other.functionName, show=False, plt=time_plt)
        time_plt.legend(loc="upper left")
        time_plt.show()
            
    
    def compareMemory(self, xlabel="", ylabel="", title="", *argv):
        memory_plt = self.plotMemory(xlabel=xlabel, ylabel=ylabel, title=title, label=self.functionName, show=False, plt=plt)
        for other in argv:
            other.plotMemory(xlabel=xlabel, ylabel=ylabel, title=title, label=other.functionName, show=False, plt=memory_plt)
        memory_plt.legend(loc="upper left")
        memory_plt.show()
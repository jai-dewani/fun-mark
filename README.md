[![Downloads](https://pepy.tech/badge/funmark)](https://pepy.tech/project/funmark)
# FunMark 

A package to bench-mark python fun-ctions for runtime and memory usage and to using methods like plotting to view and compare the results easy!

Checkout the production branch for files used to create pypi package

## Installation  
`pip install funmark`
> Right now the library isn't uploaded to pypi so this won't work as of now 

## QuickStart

## Importing Benchmarking module of funmark
Funmark has class name Benchmark which you can import using 
```
import funmark
# Bench is an object of Benchmark class
bench = funmark.Benchmark()
```
or
```
from funmark import Benchmark
# Bench is an object of Benchmark class
bench = Benchmark()
```

## Calculating Runtime and memory consumed by a function

```
def doSomecCalculation(aList, i, j):
    '''
    doing some calculations
    '''
    return aList

bench = Benchmark()

'''
Benchmark.run() runs your function and returns time and memory used up by your function in seconds and KB
logs: True/Fasle(True by default)(not necessary) Prints information about runtime and memory after every run statment
'''

time, memory = bench.run(doSomecCalculation, aList, i, j, logs=True)

'''
Benchmark.add() saves the record to its object
The first parameter is the X-cordinate while drawing the graph, it can be anything like length of list or size of graph or equivalent
'''

bench.add(len(aList), time, memory)
```
Make Sure you do add many points with different values to get a good result while representing your data in a graph

## Plotting Time and Memory used by function in Graph
```
'''
Input:
xlabel: str, Title of X-axis
ylabel: str, Title of Y-axis
title: Title of plot
label: Label for legend in graph
show: True/False, Used to toggle the last line plt.show() | Ture -> It will plot the graph

Output:
plotObject: matplotlib.pyplot Object, you can use this object to further make changes in the plot just make sure to set show=False, If the graph is plot then you won't be able make any channges
'''
plotObject = bench.plotTime(
        xlabel="Size of array",
        ylabel="Time Taken",
        title="Time vs size of list",
        label="doSomecCalculation function",
        show=True
                )

'''
Input:
xlabel: str, Title of X-axis
ylabel: str, Title of Y-axis
title: Title of plot
label: Label for legend in graph
show: True/False, Used to toggle the last line plt.show() | Ture -> It will plot the graph

Output:
plotObject: matplotlib.pyplot Object, you can use this object to further make changes in the plot just make sure to set show=False, If the graph is plot then you won't be able make any channges
'''

plotObject = bench.plotMemory(
        xlabel="Size of array",
        ylabel="Time Taken",
        title="Time vs size of list",
        label="doSomecCalculation function",
        show=True
                )

```

## Comparing performance of two different functions
```
'''
Input:
xlabel: str, Title of X-axis
ylabel: str, Title of Y-axis
title: Title of plot

Output:
A Graph with combined plot of all Benchmark Objects passed in parameter including the one from which method is called.
'''

bench_1.compareTime(
        xlabel="Size of array",
        ylabel="Time Taken",
        title="Time vs size of list",
        bench_2,
        bench_3,
        .
        .
        bench_n
)

bench_1.compareMemory(
        xlabel="Size of array",
        ylabel="Time Taken",
        title="Time vs size of list",
        bench_2,
        bench_3,
        .
        .
        bench_n
)

```

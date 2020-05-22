import funmark
from random import randint


def timSort(argv):
    ar = argv[0]
    ar.sort()
    return ar


def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
    for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 


def quickSort(argv): 
    arr = argv[0]
    low = argv[1]
    high = argv[2]
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort([arr, low, pi-1]) 
        quickSort([arr, pi+1, high]) 
  

def mergeList(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

def mergeSort(argv):
    # print(argv)
    arr = argv[0]
    l = argv[1]
    r = argv[2]
    if l < r: 
        m = (l+(r-1))//2 
        mergeSort([arr, l, m]) 
        mergeSort([arr, m+1, r]) 
        mergeList(arr, l, m, r) 

merge = funmark.Benchmark()
quick = funmark.Benchmark()
tim = funmark.Benchmark()
i = 10
top = 10**5
while i<top:
    print(i,top)
    ar = [randint(1,10**5) for i in range(i)]
    
    time, memory = merge.run(quickSort, ar, 0, len(ar)-1)
    merge.add(len(ar), time, memory)
    
    time, memory= quick.run(mergeSort, ar, 0, len(ar)-1)
    quick.add(len(ar), time, memory)

    time, memory = tim.run(timSort, ar)
    tim.add(len(ar), time, memory)

    i = int(2*i)

merge.compare("Length", "Time", "Sort comparision", quick, tim)
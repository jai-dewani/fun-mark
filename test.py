from main import Benchmark
from random import randint

def s1(argv):
    ar = argv[0]
    ar.sort()
    return ar

def merge(arr, l, m, r): 
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

def s2(argv):
    arr = argv[0]
    l = argv[1]
    r = argv[2]
    if l < r: 
        m = (l+(r-1))//2 
        s2([arr, l, m]) 
        s2([arr, m+1, r]) 
        merge(arr, l, m, r) 
  
test1 = Benchmark()
test2 = Benchmark()
i = 10
top = 10**4
while i<top:
    print(i,top)
    ar = [randint(1,10**5) for i in range(i)]
    time = test1.run(s1,ar)
    test1.add(len(ar),time)
    time = test2.run(s2, ar, 0, len(ar)-1)
    test2.add(len(ar),time)
    i = int(2*i)
test1.compare("Length", "Time", "Sort comparision", test2)
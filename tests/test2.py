# import random
# import time

# class MyTimer():

#     def __init__(self):
#         self.start = time.time()

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         end = time.time()
#         runtime = end - self.start
#         msg = 'The function took {time} seconds to complete'
#         print(msg.format(time=runtime))


# def long_runner():
#     for x in range(5):
#         sleep_time = random.choice(range(1,5))
#         time.sleep(sleep_time)

# def sort(ar):
#     ar.sort()
#     return ar

# if __name__ == '__main__':
#     for i in range(2,7):
#         with MyTimer():
#             ar = [random.randint(1,10**3) for i in range(10**i)]
#             sort(ar)

# ---------------------------------------------------------------


# import random
# import time

# def timerfunc(func):
#     """
#     A timer decorator
#     """
#     def function_timer(*args, **kwargs):
#         """
#         A nested function for timing other functions
#         """
#         start = time.time()
#         value = func(*args, **kwargs)
#         end = time.time()
#         runtime = end - start
#         msg = "The runtime for {func} took {time} seconds to complete"
#         print(msg.format(func=func.__name__,
#                          time=runtime))
#         return value
#     return function_timer


# @timerfunc
# def long_runner():
#     for x in range(5):
#         sleep_time = random.choice(range(1,5))
#         time.sleep(sleep_time)

# @timerfunc
# def sort(ar):
#     ar.sort()
#     return ar

# if __name__ == '__main__':
#     for i in range(2,7):
#         ar = [random.randint(1,10**3) for i in range(10**i)]
#         sort(ar)

# ----------------------------------------------------------------


# import matplotlib.pyplot as plt
# ar1 = [1,2,3,4]
# ar2 = [25,7,0,2]
# ar3 = [16,74,36,22]
# ar4 = [1,2,3,4]

# def test1():
#     plt.plot(ar1,ar2)
#     return plt

# def test2(plt):
#     plt.plot(ar1,ar3)
#     # plt.show()
#     return plt 

# temp = test1()
# temp = test2(temp)
# temp.plot(ar1,ar4)
# temp.show()
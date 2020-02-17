import numpy.random
import random 


# We can also import code from scipy to calculate binomial coefficients and
# factorials. NOTE: you don't need this for the birthday simulation code in Task
# 2.1, I just mention it here because you can use it to calculate the numerical
# values for the questions in section 1.
# from scipy.special import binom, factorial

# binom(n, k) computes "n choose k":
# print(binom(3, 1))
# print(binom(4, 2))

# factorial(n) computes n!
# print("5! =", factorial(5))
# print("10! =", factorial(10))


### WARNING WARNING WARNING ###

# There is also a random.randint(low, high) function in the default python
# library which returns random integers such that low <= n <= high. (whereas
# numpy's version requires < high instead). So, be mindful of which version you
# are using and the differences!

###############################

def birthday(n, k, c):
    times_repeated = 1
    list_nums = []
    repeated_nums = []
    for i in range(0, k):
        list_nums.append(random.randint(1, n))
        alreadyThere = False
        for j in range(0, i):
            if (list_nums[j] == list_nums[i]):
                for m in range(0, len(repeated_nums)):
                    if (list_nums[i] == repeated_nums[m][0] and not alreadyThere):
                        value_times_repeated = repeated_nums[m][1] + 1
                        repeated_nums.append((list_nums[i], value_times_repeated))
                        repeated_nums.remove((list_nums[i], value_times_repeated - 1))
                        alreadyThere = True
                        if (repeated_nums[m][1] > times_repeated):
                            times_repeated = repeated_nums[m][1]
                if (not alreadyThere):
                    repeated_nums.append((list_nums[i], 2))
                    if (2 > times_repeated):
                        times_repeated = 2
    return times_repeated >= c


total_true = 0
n = 365
k = 20
c = 2
for i in range(0, 100000):
    if (birthday(n, k, c)):
        total_true = total_true + 1
print(n, k, c)
print("probability = ", total_true/100000.0)
total_true = 0
n = 365
k = 40
c = 2
for i in range(0, 100000):
    if (birthday(n, k, c)):
        total_true = total_true + 1
print(n, k, c)
print("probability = ", total_true/100000.0)
total_true = 0
n = 365
k = 20
c = 3
for i in range(0, 100000):
    if (birthday(n, k, c)):
        total_true = total_true + 1
print(n, k, c)
print("probability = ", total_true/100000.0)
total_true = 0
n = 365
k = 40
c = 3
for i in range(0, 100000):
    if (birthday(n, k, c)):
        total_true = total_true + 1
print(n, k, c)
print("probability = ", total_true/100000.0)
total_true = 0
n = 1000
k = 20
c = 2
for i in range(0, 100000):
    if (birthday(n, k, c)):
        total_true = total_true + 1
print(n, k, c)
print("probability = ", total_true/100000.0)
total_true = 0
n = 1000
k = 40
c = 2
for i in range(0, 100000):
    if (birthday(n, k, c)):
        total_true = total_true + 1
print(n, k, c)
print("probability = ", total_true/100000.0)
total_true = 0
n = 1000
k = 20
c = 3
for i in range(0, 100000):
    if (birthday(n, k, c)):
        total_true = total_true + 1
print(n, k, c)
print("probability = ", total_true/100000.0)
total_true = 0
n = 1000
k = 40
c = 3
for i in range(0, 100000):
    if (birthday(n, k, c)):
        total_true = total_true + 1
print(n, k, c)
print("probability = ", total_true/100000.0)

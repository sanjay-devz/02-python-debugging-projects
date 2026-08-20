# import math
# factor = math.factorial(5)
# print(factor)


def factorial(num):
    result = 1
    for i in range(2,num + 1):
        result *= i
    return result
    
A = factorial(4)
print(A)

def factorial(n):
    '''
    There are two important items in a recursive function
    1. The base case, that exits the function
    2. The recursive step, that adds to the call stack

    When starting a recursive function, first determine
    the base case, then the recursive step

    Recursive functions don't reducve the time complexity,
    they just make the code simpler
    but they also increase the size of the call stack
    '''
    if n == 0:   return 1 #The base case, that exits the function
    return factorial(n-1)*n #The recursive step, that adds to the call stack


def factorial_tailed(n:int):
    if n == 0: return 1
    print(n)
    res = factorial(n-1)*n
    print(n)
    return res


print(factorial(5))
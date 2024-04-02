def fibonacci(n):
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
    if n == 0 or  n == 1:   return 1 #The base case, that exits the function
    return fibonacci(n-2)+fibonacci(n-1) #The recursive step, that adds to the call stack

#   0, 1, 2, 3, 4, 5, 6,  7,  8,  9,  10, 11,
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……

print(fibonacci(0))
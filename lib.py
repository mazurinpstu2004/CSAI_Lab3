import numpy as np

def fibonacci(n):
    if n <= 0:
        raise ValueError("need n > 0")
    fib_arr = np.zeros(n)
    fib_arr[1] = 1
    for i in range(2, n):
        fib_arr[i] = fib_arr[i - 2] + fib_arr[i - 1]
    return fib_arr

def bubble_sort(array):
    if len(array) <= 0:
        raise ValueError("Null array")
    if len(array) <= 0:
        raise
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

def calculator(numb1, numb2, operator):
    result = 0
    if operator == '+':
        result = numb1 + numb2
    elif operator == '-':
        result = numb1 - numb2
    elif operator == '*':
        result = numb1 * numb2
    elif operator == '/':
        if numb2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = numb1 / numb2
    else:
        raise ValueError("Invalid operator" , operator)
    return result

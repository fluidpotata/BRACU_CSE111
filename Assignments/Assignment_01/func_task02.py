''''''
'''
Write a function which will take 3 arguments minimum, maximum and divisor. You have to find all the numbers that are
divisible by the divisor where minimum value is inclusive and maximum value is exclusive. Add all the numbers and return
the value.
========================================================================================================================
Sample Input    Sample Output
(0, 10, 2)            20
(3, 16, 3)            45
'''

def argssum(min,max,div):
    sum = 0
    for i in range(min,max):
        if i%div== 0:
            sum+=i

    print(sum)


argssum(0, 10, 2)
argssum(3, 16, 3)
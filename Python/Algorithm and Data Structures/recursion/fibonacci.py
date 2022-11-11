def fib(n):
    if n <= 1 :
        return n
    else:
        sum = fib(n-1) + fib(n-2)
        return sum

print(fib(10))

'''

### Dynamically

In the form it is implemented here, the cache is set beforehand and is based on the desired **n** 
number of the Fibonacci Sequence. Note how we check it the cache[n] != None, 
meaning we have a check to know wether or not to keep setting the cache 
(and more importantly keep cache of old results!)

'''

# Instantiate Cache information
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Check cache
    if cache[n] != None:
        return cache[n]
    
    # Keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    
    return cache[n]
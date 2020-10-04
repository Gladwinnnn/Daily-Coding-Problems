# Normal recursion
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(4))
print('----------------')

# Recursion with Dynamic Programming (Memoization)
memo = {}
memo[0] = 0
def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    memo[n] = result
    return memo[n]
print(fibonacci_memo(8))
print('----------------')

# Recursion with Dynamic Programming (Bottom-up)
bottom_up = {}
bottom_up[0] = 0
def fibonacci_bottomup(n):
    # some code here
    for i in range(1,n+1):
        if i <= 2:
            result = 1
        else:
            result = fibonacci_bottomup(n-1) + fibonacci_bottomup(n-2)
        bottom_up[i] = result
    return bottom_up[i]
print(fibonacci_bottomup(9))
print('----------------')
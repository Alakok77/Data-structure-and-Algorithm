"""mod doc"""
def fibonacci(n):
    """doc"""
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(input())))

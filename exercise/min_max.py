"""find min max"""
def min_max(n):
    """doc"""
    result = []
    if n == "End":
        return result
    result.append(n)
    return min_max(input())

print(min_max(input()))

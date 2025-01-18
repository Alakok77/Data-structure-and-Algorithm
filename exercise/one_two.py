"""mod doc"""
def one_two(n):
    """doc"""
    result = ""
    sn = int(n)
    if sn in (1, 2):
        return str(n)
    result += one_two(sn-1) + one_two(sn-2)
    return result

print(one_two(input()))

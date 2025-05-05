"""mod doc"""
def hashing():
    """doc"""
    source = [111, 113, 116, 117, 118, 119, 123, 133, 143]
    lst = [0 for _ in range(10)]
    step = 1
    for i in source:
        key = i%10
        if lst[key] == 0:
            lst[key] = i
        else:
            while lst[key] != 0:
                key = (key + step)%10
            lst[key] = i
    print(*lst)

hashing()

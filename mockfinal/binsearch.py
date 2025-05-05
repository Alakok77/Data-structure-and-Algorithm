"""mod doc"""
def binary_search():
    """doc"""
    lst = [10, 20, 30, 40 ,50, 60, 70, 80, 90, 100]
    target = 60
    begin = 0
    end = len(lst) - 1

    while begin <= end:
        mid = (begin + end)//2
        if lst[mid] == target:
            print("found")
            return
        if target > lst[mid]:
            begin = mid + 1
        else:
            end = mid - 1
    print("not found")
    return


binary_search()

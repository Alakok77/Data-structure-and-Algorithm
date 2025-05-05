"""mod doc"""
def main():
    """doc"""
    lst = [1, 7, 2, 5, 1, 0, 9, 6, 3, 4, 8]
    insertion(lst ,len(lst) - 1)
    selection(lst, len(lst) - 1)
    bubble(lst, len(lst) - 1)

def insertion(lst, last):
    """insertion"""
    curr = 1
    while curr <= last:
        walker = curr - 1
        hold = lst[curr]
        while hold < lst[walker] and walker >= 0:
            lst[walker + 1] = lst[walker]
            walker -= 1
        lst[walker + 1] = hold
        curr += 1
    print(lst)

def selection(lst, last):
    """selection"""
    curr = 0
    while curr <= last:
        small = lst[curr]
        walker = curr
        while walker <= last:
            small = min(small, lst[walker])
            walker += 1
        lst[curr], small = small, lst[curr]
        curr += 1
    print(lst)

def bubble(lst, last):
    """bubble"""
    curr = 0
    is_sort = False
    while curr < last and not is_sort:
        is_sort = True
        walker = last
        while walker > curr:
            if lst[walker] < lst[walker - 1]:
                is_sort = False
                lst[walker], lst[walker - 1] = lst[walker - 1], lst[walker]
            walker -= 1
        curr += 1
    print(lst)

main()

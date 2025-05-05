import json
def insertion():
    lst = json.loads(input())
    last = int(input())
    current = 1
    walker = 0
    hold = 0
    compare = 0
    while current <= last:
        hold = lst[current]
        walker = current - 1
        while walker >= 0 and hold < lst[walker]:
            lst[walker + 1] = lst[walker]
            walker -= 1
            compare += 1
        lst[walker + 1] = hold
        if walker >= 0:
            compare += 1
        print(lst)
        current += 1
    print(f"Comparison times: {compare}")

insertion()

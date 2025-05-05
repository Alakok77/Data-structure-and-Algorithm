"""mod doc"""
import json

def card_sorting():
    """doc"""
    player = int(input())
    card = int(input())
    
    info = [json.loads(input()) for _ in range(player)]
    card_sorted = []
    
    for i in info:
        total = 0
        for j in i[1]:
            if j in ("2C", "QS"):
                total += 50
            elif "A" in j:
                total += 15
            elif "J" in j or "K" in j or "Q" in j or "10" in j:
                total += 10
            else:
                total += 5
        card_sorted.append([i[0], total, bubble_card(i[1], card)])
    
    card_sorted = bubble_point(card_sorted, player)
    for i in card_sorted:
        print(f"{i[0]} -> {i[1]} -> {i[2]}")

    
    
def bubble_card(lst, last):
    dct = {"S": 1, "H":5, "D":10, "C":15,}
    pdct = {"A":1, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}
    curr = 0
    temp = 0
    is_sort = False
    while curr < last - 1 and not is_sort:
        walker = last - 1
        is_sort = True
        while walker > curr:
            if dct[lst[walker][-1]] == dct[lst[walker - 1][-1]]:
                if pdct[lst[walker][0:-1]] > pdct[lst[walker - 1][0:-1]]:
                    is_sort = False
                    temp = lst[walker]
                    lst[walker] = lst[walker - 1]
                    lst[walker - 1] = temp
            elif dct[lst[walker][-1]] < dct[lst[walker - 1][-1]]:
                is_sort = False
                temp = lst[walker]
                lst[walker] = lst[walker - 1]
                lst[walker - 1] = temp
            walker -= 1
        curr += 1
    return lst

def bubble_point(lst, last):
    curr = 0
    temp = 0
    is_sorted = False
    while curr < last - 1 and not is_sorted:
        walker = last - 1
        is_sorted = True
        while walker > curr:
            if lst[walker][1] == lst[walker - 1][1]:
                if lst[walker][0] > lst[walker - 1][0]:
                    is_sorted = False
                    temp = lst[walker]
                    lst[walker] = lst[walker - 1]
                    lst[walker - 1] = temp
            elif lst[walker][1] > lst[walker - 1][1]:
                is_sorted = False
                temp = lst[walker]
                lst[walker] = lst[walker - 1]
                lst[walker - 1] = temp
            walker -= 1
        curr += 1
    return lst

card_sorting()
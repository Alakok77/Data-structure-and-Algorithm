import json

def knapsack():
    itemlist = json.loads(input())
    amount = int(input())
    num = len(itemlist)

    cell = [[0] * (amount + 1) for _ in range(num + 1)]

    for i in range(1, num + 1):
        name, value, weight = itemlist[i - 1]
        for j in range(amount + 1):
            if j < weight:
                cell[i][j] = cell[i - 1][j]
            else:
                cell[i][j] = max(cell[i - 1][j], value + cell[i - 1][j - weight])

    total = cell[num][amount]
    print(f"Total: {total}")

    result = []
    j = amount

    for i in range(num, 0, -1):
        name, value, weight = itemlist[i - 1]

        if j >= weight and cell[i][j] == cell[i - 1][j - weight] + value:
            result.append((name, value, weight))
            j -= weight

    result.sort(key=lambda x: x[0])

    for name, value, weight in result:
        print(f"{name} -> {weight} kg -> {value} THB")

knapsack()

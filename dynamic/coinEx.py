import json

def coinEx():
    amount = int(input())
    coins = json.loads(input())
    coin_list = [(int(k), v) for k, v in coins.items()]

    cell = [float('inf')] * (amount + 1)
    cell[0] = 0
    coin_used = [{} for _ in range(amount + 1)]
    coin_used[0] = {str(k): 0 for k in coins}

    for value, count in coin_list:
        temp_cell = cell[:]
        temp_used = [c.copy() for c in coin_used]

        for i in range(amount + 1):
            if cell[i] != float('inf'):
                for j in range(1, count + 1):
                    new_amount = i + (j * value)
                    if new_amount <= amount:
                        if temp_cell[new_amount] > cell[i] + j:
                            temp_cell[new_amount] = cell[i] + j
                            temp_used[new_amount] = coin_used[i].copy()
                            temp_used[new_amount][str(value)] = temp_used[new_amount].get(str(value), 0) + j  # ป้องกัน KeyError
        cell = temp_cell
        coin_used = temp_used

    print(f"Amount: {amount}")
    if cell[amount] == float("inf"):
        print("Can not exchange.")
    else:
        print("Coin exchange result:")
        for coin, count in coin_used[amount].items():
            print(f"  {coin} baht = {count} coins")
        print(f"Number of coins: {cell[amount]}")

coinEx()

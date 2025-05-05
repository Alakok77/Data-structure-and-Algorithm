def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def main():
    import json
    amount = int(input())
    a_first = amount
    data = convert_key(json.loads(input()))
    cnt = {}
    temp = 0
    total = 0
    
    for i in data:
        for j in range(data[i]):
            if amount < i:
                break
            amount -= i
            temp += 1
        cnt[i] = temp
        total += temp
        temp = 0
    
        
    print(f"Amount: {a_first}")
    if amount > 0:
        print("Coins are not enough.")
    else:
        print("Coin exchange result: ")
        for i in cnt:
            print(f"  {i} baht = {cnt[i]} coins")
        print(f"Number of coins: {total}")
main()
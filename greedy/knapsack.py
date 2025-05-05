class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_weight(self):
        return self.weight
    
    def get_cost(self):
        return self.price / self.weight
    
def knapsack(item_list, amount):
    dct = {}
    result = []
    a_first = amount
    total = 0
    for i in item_list:
        dct[i] = i.get_cost()
    sorted_dct = dict(sorted(dct.items(), key=lambda x: x[1], reverse=True))
    for i in sorted_dct:
        if amount - i.get_weight() > 0:
            amount -= i.get_weight()
            result.append(i)
            total += i.get_price()
    print(f"Knapsack Size: {a_first} kg")
    print("===============================")
    for i in result:
        print(f"{i.get_name()} -> {i.get_weight()} kg -> {i.get_price()} THB")
    print(f"Total: {total} THB")

def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_it = json.loads(input())
        items.append(Item(item_it['name'], item_it['price'], item_it['weight']))
        num_items = num_items - 1
    knapsack_capasity = float(input())
    knapsack(items, knapsack_capasity)
main()
    
"""mod doc"""
class LeawTea:
    """doc"""
    def __init__(self):
        self.menu = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]
        self.cnt = 0

    def random(self):
        """doc"""
        self.cnt += 1

    def list_food(self):
        """doc"""
        self.menu.sort(key=str)
        print(self.menu)

def main():
    """doc"""
    food = LeawTea()
    food.list_food()

main()

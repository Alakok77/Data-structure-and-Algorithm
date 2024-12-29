"""mod doc"""
class Elevator:
    """class"""
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        """go to floor"""
        self.current_floor = floor

    def report_current_floor(self):
        """report"""
        print(self.current_floor)

def main():
    """doc"""
    elevator = Elevator(int(input()))
    while True:
        floor = input()
        if floor == "Done":
            elevator.report_current_floor()
            break
        if int(floor) > elevator.max_floor or int(floor) < 0:
            print("Invalid Floor!")
        else:
            elevator.go_to_floor(int(floor))
main()

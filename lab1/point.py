class Point:
    """point"""
    def __init__(self, x=0, y=0):
        self.set_coordinates(x, y)

    def set_coordinates(self, x, y):
        """set coordinates"""
        self.x = x
        self.y = y

    def get_coordinates(self):
        """get coordinates"""
        return (self.x, self.y)

    def calculate_distance(self, other_pointX, other_pointY):
        """calculate"""
        pointX = other_pointX
        pointY = other_pointY
        return f"{(((pointX - self.x)**2 + (pointY - self.y)**2) ** 0.5):.2f}"

def main():
    """doc"""
    point = Point(float(input()), float(input()))
    print(point.calculate_distance(float(input()), float(input())))

main()

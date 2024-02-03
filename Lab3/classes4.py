class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        
    def dist(self, point):
        distance = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
        return distance
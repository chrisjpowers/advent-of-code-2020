class BottomOfHillError(BaseException):
    pass


class Hill:
    @classmethod
    def parse(cls, lines):
        matrix = [
            [c == "#" for c in line.strip()] for line in lines
        ]
        return cls(matrix)
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)
    
    def tree_at(self, x, y):
        if y >= self.height:
            raise BottomOfHillError()
        return self.matrix[y][x % self.width]


class Sled:
    def __init__(self, hill, velocity, coords=(0,0)):
        self.hill = hill
        self.coords = coords
        self.velocity = velocity
        self.trees = 0
    
    def run(self):
        x,y = self.coords
        if y >= self.hill.height:
            return
        if self.hill.tree_at(x, y):
            self.trees += 1
        self.coords = (self.coords[0] + self.velocity[0], self.coords[1] + self.velocity[1])
        self.run()
    
    def report(self):
        print(f"Hit {self.trees} trees")

if __name__ == '__main__':
    with open("day-03/input.txt") as file:
        hill = Hill.parse(file)
    sled = Sled(hill, (3,1))
    sled.run()
    sled.report()
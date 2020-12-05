class BinarySeat:
    def __init__(self, code):
        self.code = code
    
    @property
    def number(self):
        bin_rep = self.code.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        return eval(f"0b{bin_rep}")

if __name__ == '__main__':
    with open('day-05/input.txt') as file:
        highest_id = 0
        for line in file:
            seat = BinarySeat(line.strip()).number
            if seat > highest_id: highest_id = seat
    print(f"Highest seat: {highest_id}")
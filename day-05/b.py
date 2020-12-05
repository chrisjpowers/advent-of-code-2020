from a import BinarySeat

if __name__ == '__main__':
    with open('day-05/input.txt') as file:
        seats = []
        for line in file:
            seat = BinarySeat(line.strip()).number
            seats.append(seat)

    last_seat = 0
    for seat in sorted(seats):
        if seat == last_seat + 2:
            print(f"Your seat: {last_seat + 1}")
            exit(0)
        last_seat = seat
    print("No seat found :(")
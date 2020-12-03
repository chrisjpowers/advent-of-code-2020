from a import Hill, Sled



if __name__ == '__main__':
    with open("day-03/input.txt") as file:
        hill = Hill.parse(file)
    velocities = [
        (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)
    ]
    product = 1
    for vel in velocities:
        sled = Sled(hill, vel)
        sled.run()
        sled.report()
        product = product * sled.trees
    
    print(f"Final product: {product}")
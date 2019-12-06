import numpy as np

def main():
    with open('input', 'r') as f:
        wires = f.read().splitlines()
        wire0 = wires[0].split(',')
        wire1 = wires[1].split(',')
    field1 = np.zeros((10, 10), dtype=int)
    starting_point = [4, 4]
    current_point = starting_point
    wire0 = ['R2','U2','L4', 'D4']
    wire1 = ['U1','R4']
    
    field1 = print_wire(field1, starting_point, wire0)
    field1 = print_wire(field1, starting_point, wire1)
    print(field1)
    print(field1[starting_point[0], starting_point[1]])
def print_wire(field1, starting_point, wire0):
    current_point = np.copy(starting_point)
    field1[starting_point[0], starting_point[1]] = 5
    for path in wire0:
        direction = path[:1]
        distance = int(path[1:])

        if direction == "U" :
            pos1 = np.where(field1[current_point[0] - distance : current_point[0],
                   current_point[1]] == 1)[0]

            field1[current_point[0] - distance : current_point[0],
                   current_point[1]] = 1
            if pos1.size > 0 :
                field1[current_point[0] - pos1, current_point[1]] = 2
            
            current_point[0] -= distance
        elif direction == "D":
            pos1 = np.where(field1[current_point[0] + 1 : current_point[0]  +
                                   distance  + 1,
                   current_point[1]] == 1)[0] + 1

            field1[current_point[0] + 1 : current_point[0] + distance + 1,
                   current_point[1]] = 1
            if pos1.size > 0 :
                field1[current_point[0] + pos1, current_point[1]] = 2

            current_point[0] += distance
        elif direction == "R":
            pos1 = np.where(field1[current_point[0], current_point[1] + 1: current_point[1]
                    + distance + 1] == 1)[0] + 1

            field1[current_point[0], current_point[1] + 1: current_point[1]
                    + distance + 1] = 1
            if pos1.size > 0 :
                field1[current_point[0], current_point[1] + pos1] = 2

            current_point[1] += distance
        elif direction == "L":
            pos1 = np.where(np.flip(field1[current_point[0], current_point[1] - distance :
                   current_point[1]], 0) == 1)[0] + 1

            field1[current_point[0], current_point[1] - distance :
                   current_point[1]] = 1
            if pos1.size > 0 :
                field1[current_point[0], current_point[1] - pos1] = 2

            current_point[1] -= distance
    return(field1)


if __name__ == "__main__":
    main()

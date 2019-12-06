import numpy as np

def main():
    with open('input', 'r') as f:
        wires = f.read().splitlines()
        wire0 = wires[0].split(',')
        wire1 = wires[1].split(',')
    field1 = np.zeros((30000, 30000), dtype=int)
    starting_point = [10000, 10000]
    current_point = starting_point
    
    field1 = print_wire(field1, starting_point, wire0)
    field1 = print_wire(field1, starting_point, wire1)
    find2 = np.where(field1 == 2)
    zipped = np.concatenate((np.array(find2[0]), np.array(find2[1])))
    #print(zipped)
    find2_x = find2[0]
    find2_y = find2[1]
    
    distances= []
    for i in range(len(find2_x)):
        distance = abs(find2_x[i] - starting_point[0]) + abs(find2_y[i] -
                                                             starting_point[1])
        distances.append(distance)

    print(min(distances))

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

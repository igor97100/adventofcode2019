import numpy as np

def main():
    input_np = np.loadtxt(fname = "input")
    fuels = [calc_fuel(x) for x in input_np]

    print(calc_fuel(12))
    print(calc_fuel(1969))
    print(np.sum(fuels))

def calc_fuel(x, fuels = np.array([])):
    fuel = x // 3 - 2 

    if fuel > 0:
        fuels = np.append(fuels, fuel)
        return calc_fuel(fuel, fuels)
    else:
        return np.sum(fuels)

if __name__ == '__main__':
    main()

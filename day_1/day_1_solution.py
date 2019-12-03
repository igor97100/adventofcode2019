import numpy as np

def main():
    input_np = np.loadtxt(fname = "input")
    fuels = calc_mass(input_np) 
    print(masses) 

def calc_fuel(x):
    fuel = x // 3 - 2 
    return fuel

if __name__ == '__main__':
    main()

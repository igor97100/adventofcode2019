import numpy as np

def main():
    input_np = np.loadtxt(fname = "input")
    print(input_np)
    masses = calc_mass(input_np) 
    print(masses) 

def calc_mass(x):
    mass = x // 3 - 2 

if __name__ == '__main__':
    main()

import numpy as np

def main():
  seq = np.loadtxt(fname = 'input', delimiter = ',', dtype= np.uint16)
  print(seq[0])

if __name__ == '__main__':
    main()

import numpy as np

def main():
    seq = np.loadtxt(fname = 'input', delimiter = ',', dtype= np.uint64)
    seq[1] = 12
    seq[2] = 2
    print(seq) 
    for i in range(0, len(seq), 4):

        opcode = seq[i]
        if opcode == 99:
            break
        elif opcode == 1:
            seq[seq[i+3]] = seq[seq[i+1]] + seq[seq[i+2]]
            print(f'seq[{i+3}] became {seq[i+3]}')
        elif opcode == 2:
            seq[seq[i+3]] = seq[seq[i+1]] * seq[seq[i+2]]
        else:
            print(f'opcode {opcode} at position {i} is invalid')
            break
    
    print(seq[0])

if __name__ == '__main__':
    main()

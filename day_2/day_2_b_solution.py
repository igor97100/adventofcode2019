import numpy as np

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

def main():
    #for noun in range(100):
     #   for verb in range(100):
      #      if(verb % 20 == 0):
       #         print(run_intcode(noun, verb))
    print(run_intcode(5, 10))

def run_intcode(noun, verb):
    seq = init_intcode()
    if seq[0] == 4023471:
        print('the program was initialized correctly')
    else:
        raise Error('the program was not initilized correctly')
    seq[1] = noun
    seq[2] = verb
    for i in range(0, len(seq), 4):
        opcode = seq[i]
        if opcode == 99:
            break
        elif opcode == 1:
            seq[seq[i+3]] = seq[seq[i+1]] + seq[seq[i+2]]
        elif opcode == 2:
            seq[seq[i+3]] = seq[seq[i+1]] * seq[seq[i+2]]
        else:
            break
    return seq[0]
 
def init_intcode():
    seq = np.loadtxt(fname = 'input', delimiter = ',', dtype= np.uint64)
    seq[1] = 12
    seq[2] = 2
    for i in range(0, len(seq), 4):
        opcode = seq[i]
        if opcode == 99:
            break
        elif opcode == 1:
            seq[seq[i+3]] = seq[seq[i+1]] + seq[seq[i+2]]
        elif opcode == 2:
            seq[seq[i+3]] = seq[seq[i+1]] * seq[seq[i+2]]
        else:
            break
    return seq
 

if __name__ == '__main__':
    main()

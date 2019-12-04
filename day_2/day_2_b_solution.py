import numpy as np

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

def main():
    seq = np.loadtxt(fname = 'input', delimiter = ',', dtype= np.uint64)
    for noun in range(100):
        for verb in range(100):
            out = run_intcode(seq, noun, verb) 
            if(out == 19690720):
                print(100 *  noun + verb)
                break
    

def run_intcode(original_seq, noun, verb):
    seq = np.copy(original_seq)
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

    if seq[0] != 4023471:
        raise Error('the program was not initilized correctly')

    return seq

if __name__ == '__main__':
    main()

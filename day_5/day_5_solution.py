import numpy as np

class Error(Exception):
    """Base class for exceptions in this module."""
    pass


def main():
    input_ = np.loadtxt(fname = 'input', delimiter = ',', dtype=np.int64)

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
 
if __name__ == '__main__':
    main()

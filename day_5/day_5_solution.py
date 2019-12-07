import numpy as np

class Error(Exception):
    """Base class for exceptions in this module."""
    pass


def main():
    input_ = np.loadtxt(fname = 'input', delimiter = ',', dtype=np.int64)


def run_intcode(original_seq, only_input):
    seq = np.copy(original_seq)
    i = 0
    opcode = seq[0]
    while opcode != 99:
        if opcode == 3:
            seq[seq[i+1]] = only_input
            i += 2
        elif opcode == 4:
            print(f'Opcode 4 output: {seq[seq[i+1]]}}')
            i += 2
        else:

            unmerged_opcode = map(int, str(opcode))
            while len(unmerged_opcode != 5):
                unmerged_opcode.insert(0, 0)
        opcode = seq[i]
    return seq[0]
 
if __name__ == '__main__':
    main()

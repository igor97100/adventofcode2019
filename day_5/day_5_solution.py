import numpy as np

class Error(Exception):
    """Base class for exceptions in this module."""
    pass


def main():
    input_ = np.loadtxt(fname = 'input', delimiter = ',', dtype=np.int64)
    print
    input_ = np.concatenate((input_, np.zeros(1000, dtype = np.int64)))    
    run_intcode(input_, 1)

def run_intcode(original_seq, only_input):
    seq = np.copy(original_seq)
    i = 0
    opcode = seq[0]
    while opcode != 99:
        if opcode == 3:
            seq[seq[i+1]] = only_input
            i += 2
            
        elif opcode == 4:
            print(f'Opcode 4 output: {seq[seq[i+1]]}')
            i += 2
        else:

            unmerged_opcode = list(map(int, str(opcode)))
            while len(unmerged_opcode) != 5:
                unmerged_opcode.insert(0, 0)
            print(unmerged_opcode)
            param1 = seq[seq[i+1]] if unmerged_opcode[2] == 0 else seq[i+1]
            param2 = seq[seq[i+2]] if unmerged_opcode[1] == 0 else seq[i+2]
            param3 = seq[i+3] if unmerged_opcode[0] == 0 else i+3
            if unmerged_opcode[4] == 1:
                seq[param3] = param1 + param2
                print(param1, param2, param3)
            elif unmerged_opcode[4] == 2:
                seq[param3] = param1 * param2
            else:
                print(i, opcode)
                print('ERROR !! Not recognized opcode')
            i+= 4

        opcode = seq[i]
    return seq[0]
 
if __name__ == '__main__':
    main()

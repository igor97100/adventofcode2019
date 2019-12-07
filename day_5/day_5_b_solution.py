import numpy as np

class Error(Exception):
    """Base class for exceptions in this module."""
    pass


def main():
    input_ = np.loadtxt(fname = '/Users/igor/adventofcode2019/day_5/input', delimiter = ',', dtype=np.int64)
    #input_ = np.array([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
    input_ = np.concatenate((input_, np.zeros(10000, dtype = np.int64)))    
    run_intcode(input_, 5)

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
            param1 = seq[seq[i+1]] if unmerged_opcode[2] == 0 else seq[i+1]
            param2 = seq[seq[i+2]] if unmerged_opcode[1] == 0 else seq[i+2]
            param3 = seq[i+3] if unmerged_opcode[0] == 0 else i+3
            if unmerged_opcode[4] == 1:
                seq[param3] = param1 + param2
            elif unmerged_opcode[4] == 2:
                seq[param3] = param1 * param2
            elif unmerged_opcode[4] == 5:
                if param1 != 0:
                    i = param2
                    opcode = seq[i]
                    continue
                else:
                    i += 3
                    opcode = seq[i]
                    continue

            elif unmerged_opcode[4] == 6:
                if param1 == 0:
                    i = param2
                    opcode = seq[i]
                    continue
                else:
                    i += 3
                    opcode = seq[i]
                    continue

            elif unmerged_opcode[4] == 7:
                if param1 < param2 :
                    seq[param3] = 1
                else:
                    seq[param3] = 0
            elif unmerged_opcode[4] == 8:
                if param1 == param2 :
                    seq[param3] = 1
                else:
                    seq[param3] = 0

            else:
                print(i, opcode)
                print('ERROR !! Not recognized opcode')
            i+= 4

        opcode = seq[i]
    return seq[0]
 
if __name__ == '__main__':
    main()

import collections
from operator import itemgetter
class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
    
    def calc(self):
        self.parent.calc
    
    def get_parent(self):
        return self.parent



def main():
    input_ = open('/Users/igor/adventofcode2019/day_6/input', 'r').read().splitlines()
    #input_ = [ 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H','D)I', 'E)J', 'J)K' ,'K)L']
    

    left = [x[:3] for x in input_]
    right = [x[4:] for x in input_]
    

    deduplicated_left = list(set(left))
    
    parent = Node('saf', 1).get_parent()
    print(parent)
    nodes = []
    for i, item in enumerate(left):
        
        nodes.append(Node(right[i], deduplicated_left.index(item)))

    total = 0
    nodes.append(Node('COM', -99))
    for node in nodes:
        
        if node.value != 'COM':
            node_total = 1
            parent = [x for x in nodes if x.value == deduplicated_left[node.parent]][0]
            while parent.value != 'COM':
                node_total += 1
                parent = [x for x in nodes if x.value == deduplicated_left[parent.parent]][0]
            total += node_total
    print(total)
            
if __name__ == '__main__':
    main()

   
class TrieNode:
    def __init__(self):
        self.child = [None] * 5
        self.wordEnd = False
        self.parent = None

def letter_idx(towel):
    match towel:
        case 'w':
            return 0
        case 'u':
            return 1
        case 'b':
            return 2
        case 'r':
            return 3
        case 'g':
            return 4
        
        case _:
            print('?')
            return ord(towel) # would return an error on retrieval anyway

def add_word(root, key):
    curr = root
    for c in key:
        
        i = letter_idx(c)
        if curr.child[i] == None:
            new_node = TrieNode()
            curr.child[i] = new_node
            
        curr = curr.child[i]
    curr.wordEnd = True

from functools import cache


@cache
def count_combos(root, key):               
    
    # print(key)
    curr = root
    n = len(key)
    combos = 0
    
    if n == 0:
        return 1 # True for valid combo
    
    for i in range(n):
        next = letter_idx(key[i])
        
        if curr.child[next] is not None:       
            curr = curr.child[next]
        else:
            return combos # False, or possible combos from earlier cycles
        
        if curr.wordEnd:
            res = count_combos(root, key[i+1:])
            if res:
                combos += res # increment for true
         
    # ending on a non-terminal, non-word node is not valid
    return combos

    
    
if __name__ == '__main__':
    
    p1 = 0
    p2 = 0
    TrieRoot = TrieNode()
    
    with open('input.txt') as f:
        patterns = f.readline().strip().split(', ')
        for p in patterns:
            # print("inserting {}".format(p))
            add_word(TrieRoot, p.strip())
            
        f.readline() # skip empty line
        
        # rest of lines are designs
        for line in f.readlines():
            
            # check if part of the design exists in a trie of existing towels
            design = line.strip()
            i = 0
            # keep advancing search with index or stop search
            pos = count_combos(TrieRoot, design)
            if pos:
                p1 += 1
                p2 += pos
                
                        
    print("Part 1: {}\nPart 2: {}".format(p1, p2))
        
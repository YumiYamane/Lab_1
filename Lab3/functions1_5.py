from itertools import permutations 

def Permutations(s):
    a = permutations(s)
    for permutation in a: 
        print(str().join(permutation))
        
s = input()
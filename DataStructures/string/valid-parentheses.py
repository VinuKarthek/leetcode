https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        #open_paranthesis_list = ['(','[','{']
        #pair_dct = {'tuple':['(',')'], 'list':['[',']'], 'dict':['{','}']}
        pair_dct = {'[':']','(':')','{':'}' }
        memory = ''
        
        if not len(s)>1: return False 
        for char in s:
            #print(char)
            if pair_dct.get(char):
                memory = memory+ char
            else:
                if pair_dct.get(memory[-1:]) == char:
                    memory = memory[:-1]
                else:
                    return False
        
        #if len(memory) ==0: return True
        return len(memory) == 0


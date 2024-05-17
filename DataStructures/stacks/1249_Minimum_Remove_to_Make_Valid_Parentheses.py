import unittest
import time

#1768. Merge Strings Alternately
#URL --> https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for idx in range(len(s)):
            if s[idx] == '(':
                stack.append(idx)
            elif s[idx] == ')' :
                if stack :
                    stack.pop()
                else:
                    s[idx] = ""
        
        while stack:
            s[stack.pop()] = ''                
        return ''.join(s)
        

class TestSolution(unittest.TestCase):
    
    def time_it(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"{func.__name__} executed in {execution_time:.4f} seconds")
            return result
        return wrapper

    def setUp(self):
        self.solution = Solution()
        self.method = self.solution.minRemoveToMakeValid
    
    @time_it
    def test_case1(self):
        self.assertEqual(self.method('lee(t(c)o)de)'), "lee(t(c)o)de")
    
    @time_it
    def test_case2(self):
        self.assertEqual(self.method('a)b(c)d'), "ab(c)d")

    @time_it
    def test_case3(self):
        self.assertEqual(self.method('))(('), "")

if __name__ == "__main__":
    unittest.main()

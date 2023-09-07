import unittest
import time

#2390. Removing Stars From a String
'''
Use two stack one for result and another as temporary
'''
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            # if ch == '*' and len(stack)>0: 220ms
            if ch == '*' and stack: #180ms
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)

        

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
        self.method = self.solution.removeStars

    @time_it
    def test_case1(self):
        self.assertEqual( self.method("leet**cod*e"), "lecoe")
    
    @time_it
    def test_case2(self):
        self.assertEqual(self.method("erase*****"), "")

    @time_it
    def test_case3(self):
        self.assertEqual(self.method("****************"), "")

if __name__ == "__main__":
    unittest.main()

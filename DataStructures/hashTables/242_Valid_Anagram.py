#242. Valid Anagram
#https://leetcode.com/problems/valid-anagram/

import unittest,  time
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count = defaultdict(int)
        for s_val, t_val in zip(s, t):
            count[s_val] += 1
            count[t_val] -= 1
        # Check if any character has non-zero frequency
        return all(v == 0 for v in count.values())

class TestSolution(unittest.TestCase):

    def time_it(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            print(f"{func.__name__} executed in {execution_time:.6f} seconds")
            return result
        return wrapper

    def setUp(self):
        self.solution = Solution()
        self.method = self.solution.isAnagram

    @time_it
    def test_case1(self):
        self.assertEqual( self.method(s = "anagram", t = "nagaram"), True)
        
    @time_it
    def test_case2(self):
        self.assertEqual( self.method(s = "car", t = "rat"), False )

    @time_it
    def test_case3(self):
        self.assertEqual( self.method(s = "abcd", t = "pq"), False )

    @time_it
    def test_case4(self):
        self.assertEqual( self.method(s = "carrace", t = "racecar"), True)

if __name__ == "__main__":
    unittest.main()
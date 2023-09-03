import unittest
import time

#1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def time_it(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"{func.__name__} executed in {execution_time:.4f} seconds")
            return result
        return wrapper
    
    @time_it
    def test_case1(self):
        word1 = "ab"
        word2 = "pqrs"
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, "apbqrs")
    
    @time_it
    def test_case2(self):
        word1 = "abc"
        word2 = "pqr"
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, "apbqcr")

    @time_it
    def test_case3(self):
        word1 = "abcd"
        word2 = "pq"
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, "apbqcd")

    @time_it
    def test_case4(self):
        word1 = ""
        word2 = ""
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()

import unittest
import time

#1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return
        

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
        self.method = self.solution.mergeAlternately
    
    @time_it
    def test_case1(self):
        word1 = "ab"
        word2 = "pqrs"
        self.assertEqual(self.method(word1, word2), "apbqrs")
    
    @time_it
    def test_case2(self):
        word1 = "abc"
        word2 = "pqr"
        self.assertEqual(self.method(word1, word2), "apbqcr")

    @time_it
    def test_case3(self):
        word1 = "abcd"
        word2 = "pq"
        self.assertEqual(self.method(word1, word2), "apbqcd")

    @time_it
    def test_case4(self):
        word1 = ""
        word2 = ""
        self.assertEqual(self.method(word1, word2), "")

if __name__ == "__main__":
    unittest.main()

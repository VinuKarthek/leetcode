import unittest
import time
from typing import Any

#88. Merge Sorted Array

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        # Write the elements of num2 into the end of nums1.
        for i in range(n):
            nums1[i + m] = nums2[i]
        
        # Sort nums1 list in-place.
        nums1.sort()
        
        return nums1
        

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
        self.method = self.solution.merge
    
    @time_it
    def test_case1(self):
        self.assertEqual(self.method(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3), [1,2,2,3,5,6])
    
    @time_it
    def test_case2(self):
        self.assertEqual(self.method(nums1 = [1], m = 1, nums2 = [], n = 0), [1])

    @time_it
    def test_case3(self):
        self.assertEqual(self.method(nums1 = [0], m = 0, nums2 = [1], n = 1), [1])

    # @time_it
    # def test_case4(self):
    #     self.assertEqual(self.method(word1, word2), "")

if __name__ == "__main__":
    unittest.main()

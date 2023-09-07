import unittest
import time

#Bubble Sort https://codepumpkin.com/wp-content/uploads/2017/10/BubbleSort_Avg_case.gif
#Time Complexity O(n^2)
#Space Complexity O(1)



class Solution:
    @staticmethod
    def selection_sort(input_list):
        for idx in range(len(input_list)):
            min_idx = idx
            for j in range( idx +1, len(input_list)):
                if input_list[min_idx] > input_list[j]:
                    min_idx = j
            # Swap the minimum value with the compared value
            input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
        return input_list
        

class TestSolution(unittest.TestCase):
    
    def time_it(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"{func.__name__} executed in {execution_time:.6f} seconds")
            return result
        return wrapper

    def setUp(self):
        self.solution = Solution()
        self.method = self.solution.selection_sort
    
    @time_it
    def test_case1(self):
        list = [19,2,31,45,30,11,121,27]
        out = list.copy()
        out.sort()
        self.assertEqual(self.method(list), out)
    
    # @time_it
    # def test_case2(self):
    #     word1 = "abc"
    #     word2 = "pqr"
    #     self.assertEqual(self.method(word1, word2), "apbqcr")

    # @time_it
    # def test_case3(self):
    #     word1 = "abcd"
    #     word2 = "pq"
    #     self.assertEqual(self.method(word1, word2), "apbqcd")

    # @time_it
    # def test_case4(self):
    #     word1 = ""
    #     word2 = ""
    #     self.assertEqual(self.method(word1, word2), "")

if __name__ == "__main__":
    unittest.main()

import unittest
import time

#735. Asteroid Collision
'''
Use two stack one for result and another as temporary
'''
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        ans = []
        stack = []
        for x in asteroids:
            if x>0:
                stack.append(x)
            else:
                # negative asteroid destroys others in stack one by one
                while len(stack)>0 and abs(x) > stack[-1]:
                    stack.pop()
                # negative asteroid destroyed all the ones to its left
                if len(stack) == 0:
                    ans.append(x)
                else:
                    #if same magnitude both are destroyed
                    if stack[-1] == abs(x):
                        stack.pop()

        ans += stack
        return ans
        

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
        self.method = self.solution.asteroidCollision

    @time_it
    def test_case1(self):
        self.assertEqual(self.method([10,2,-5]), [10])
    
    @time_it
    def test_case2(self):
        self.assertEqual(self.method([5,10,-5]), [5,10])

    @time_it
    def test_case3(self):
        self.assertEqual(self.method([8,-8]), [])

    # @time_it
    # def test_case4(self):
    #     result = self.solution.asteroidCollision(word1, word2)
    #     self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()

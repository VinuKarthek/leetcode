import unittest, time

#224. Basic Calculator
class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        operand  = '+'
        for ch in s:
            if not ch == ' ':
                if ch.isdigit():
                    if operand == '-':
                        result -= int(ch)
                    else:
                        result += int(ch)
                else:
                    operand = ch
        return result
        
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
        self.method = self.solution.calculate

    @time_it
    def test_case1(self):
        self.assertEqual(self.method("1 + 1"), 2)

    @time_it
    def test_case2(self):
        self.assertEqual(self.method(" 2-1 + 2 "), 3)
    
    @time_it
    def test_case3(self):
        self.assertEqual(self.method("(1+(4+5+2)-3)+(6+8)"), 23)

if __name__ == "__main__":
    unittest.main()

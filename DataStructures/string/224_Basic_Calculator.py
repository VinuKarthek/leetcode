import unittest

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
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        s = "1 + 1"
        result = self.solution.calculate(s)
        self.assertEqual(result, 2)

    def test_case2(self):
        s = " 2-1 + 2 "
        result = self.solution.calculate(s)
        self.assertEqual(result, 3)

    def test_case3(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        result = self.solution.calculate(s)
        self.assertEqual(result, 23)



if __name__ == "__main__":
    unittest.main()

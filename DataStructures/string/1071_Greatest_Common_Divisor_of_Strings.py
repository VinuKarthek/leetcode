import unittest

#1071. Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        smallest_str = str1 if len(str1) >= len(str2) else str2
        gcd = ''
        for i in range(len(smallest_str)):
            gcd = smallest_str if i==0 else smallest_str[:-i]
            if str1.replace(gcd, '') == '' and  str2.replace(gcd, '') == '':
                return gcd
        return ''
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        word1 = "ABCABC"
        word2 = "ABC"
        result = self.solution.gcdOfStrings(word1, word2)
        self.assertEqual(result, "ABC")

    def test_case2(self):
        word1 = "ABABAB"
        word2 = "ABAB"
        result = self.solution.gcdOfStrings(word1, word2)
        self.assertEqual(result, "AB")

    def test_case3(self):
        word1 = "LEET"
        word2 = "CODE"
        result = self.solution.gcdOfStrings(word1, word2)
        self.assertEqual(result, "")
   
    def test_case4(self):
        word1 = "ABABABAB"
        word2 = "ABAB"
        result = self.solution.gcdOfStrings(word1, word2)
        self.assertEqual(result, "ABAB")


if __name__ == "__main__":
    unittest.main()

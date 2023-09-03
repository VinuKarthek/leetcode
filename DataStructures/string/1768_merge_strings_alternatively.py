import unittest


#1768. Merge Strings Alternately


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       
        l1 = len(word1)
        l2 = len(word2)
        merge_str = ''
        for s1, s2 in zip(word1 , word2):
            merge_str += s1+s2
        
        if not l1 == l2:
            extra_str = word1[-(l1-l2):] if l1>l2 else word2[-(l2-l1):]
            return merge_str+ extra_str
        else:
            return merge_str
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        word1 = "ab"
        word2 = "pqrs"
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, "apbqrs")

    def test_case2(self):
        word1 = "abc"
        word2 = "pqr"
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, "apbqcr")

    def test_case3(self):
        word1 = "abcd"
        word2 = "pq"
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, "apbqcd")

    def test_case4(self):
        word1 = ""
        word2 = ""
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()

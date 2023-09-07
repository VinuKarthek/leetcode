# https://leetcode.com/problems/palindrome-linked-list/description/
# 234. Palindrome Linked List
# https://www.youtube.com/watch?v=8h2UOPDCGPM&ab_channel=OneCodeMan

import unittest, time

#  Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.current  = None

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            self.current = new_node
        else:
            self.current.next = new_node
        self.current = new_node

class Solution:
    def isPalindrome(self, head) -> bool:
        current = head
        s = []
        while current:
            s.append(current.val)
            current = current.next
        rev_list = s.copy()
        rev_list.reverse()
        return (rev_list == s)

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
        list_ = [1,2,2,1]
        my_linked_list = LinkedList()
        for item in list_:
            my_linked_list.append(item)
        result = self.solution.isPalindrome(my_linked_list.head)
        self.assertEqual(result, True)
    
    @time_it
    def test_case2(self):
        list_ = [1,2,22,1]
        my_linked_list = LinkedList()
        for item in list_:
            my_linked_list.append(item)
        result = self.solution.isPalindrome(my_linked_list.head)
        self.assertEqual(result, False)

    @time_it
    def test_case3(self):
        list_ = [1,2,231]
        my_linked_list = LinkedList()
        for item in list_:
            my_linked_list.append(item)
        result = self.solution.isPalindrome(my_linked_list.head)
        self.assertEqual(result, False)

    @time_it
    def test_case4(self):
        list_ = []
        my_linked_list = LinkedList()
        for item in list_:
            my_linked_list.append(item)
        result = self.solution.isPalindrome(my_linked_list.head)
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()

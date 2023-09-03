# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list = [4,6,7]

#Create a linked list
prev_node, first_node = None, None
for item in list:
    if first_node is None:
        first_node = ListNode(val = item, next = None)
        curr_node = first_node
    else:
        curr_node = ListNode(val = item, next = None)
        prev_node.next = curr_node

    prev_node = curr_node
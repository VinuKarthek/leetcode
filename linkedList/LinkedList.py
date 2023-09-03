class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

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
            # current = self.head
            # while current.next:
            #     current = current.next
            # current.next = new_node
        self.current = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.display()  # Output: 1 -> 2 -> 3 -> None





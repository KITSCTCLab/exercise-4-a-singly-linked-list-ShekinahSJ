from typing import Optional


class Node:
    """
    Provide necessary documentation
    """
    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """
    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        # Write code here
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while (temp.next is not None):
                temp=temp.next
            temp.next=newNode

    def status(self):
        """
        It prints all the elements of list.
        """
        # write code here
        displaylist=self.head
        while displaylist!=None:
            print(displaylist.next)
            displaylist=displaylist.next
        


class Solution:
    """
    Provide necessary documentation
    """
    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        # Write code here
        head = None
        temp = None
        c = 0
        while first_list or second_list:
            if not first_list:
                a= 0
            else:
                a = first_list.Node(data)
            if not second_list:
                b=0
            else:
                b = second_list.Node(data)
            n = a +b + c
            c = 1 if n>9 else 0
            node = ListNode(n%10)
            if not head:
                head = node
                temp = node
            else:
                head.next = node
                head = node
            first_list = first_list.next if first_list else None
            second_list = second_list.next if second_list else None
        if c:
            node = ListNode(1)
            head.next = node
        return temp

# Do not edit the following code      
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()

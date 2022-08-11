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
    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[
        LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        result = self.get_num(first_list) + self.get_num(second_list)
        sum_list = LinkedList()
        for digit in list(map(int, str(result)[::-1])):
            sum_list.insert_at_end(digit)
        return sum_list

    def get_num(self, l: Optional[LinkedList]) -> int:
        """
        :param l: LinkedList with non-negative integers
        :return: returns digits of the list as a single integer
        """
        curr = l.head
        if curr is None:
            return 0
        num = ""
        while curr is not None:
            num = str(curr.data) + num
            curr = curr.next
        return int(num)

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

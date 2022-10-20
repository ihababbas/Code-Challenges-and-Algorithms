# Write here the code challenge solution
class Node:
    def __init__(self,value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def printAll(self):
        list = []
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                list.append(current.value)
                current = current.next
        print(list)
    
    def delete(self, value):
        if value is None:
            return
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.value == value:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next   
                



linkedList1 = LinkedList()
node1 = Node(4)
linkedList1.append(node1)

node2 = Node(5)
linkedList1.append(node2)

node3 = Node(1)
linkedList1.append(node3)

node4 = Node(9)
linkedList1.append(node4)

linkedList1.printAll()

linkedList1.delete(1)
linkedList1.printAll()

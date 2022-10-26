# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


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
        list =[]
        current = self.head
        while current is not None:
                list.append(current.value)
                current = current.next
        print(list)
    def deleteNode(self, n):
        first = self.head
        second = self.head
        
        for i in range(n):
             
            # If count of nodes in the
            # given list is less than 'n'
            if(second.next == None):
                
                # If index = n then
                # delete the head node
                if(i == n - 1):
                    self.head = self.head.next
                return self.head
            second = second.next
             
        while(second.next != None):
            second = second.next
            first = first.next
            
        first.next = first.next.next        
        
        



           





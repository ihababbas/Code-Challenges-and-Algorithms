# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    '''
    this class will be the construtor
    '''

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, node):
        '''
         this method will add the node that created to the linkedlist of this class
         '''
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    
    def printAll(self):
        '''
         this method willtake all added nodes from the linkied list and print them as a list
        '''
        list =[]
        current = self.head
        while current is not None:
                list.append(current.value)
                current = current.next
        print(list)
    
    def deleteNode(self, n):
        '''
        Given a linked list and an integer N, the task is to delete the Nth node from the end of the given linked list.
        '''
        first = self.head
        second = self.head
        
        for i in range(n):
            if(second.next == None):
                
                if(i == n - 1):
                    self.head = self.head.next
                return self.head
            second = second.next
             
        while(second.next != None):
            second = second.next
            first = first.next
            
        first.next = first.next.next        
        
        


'''
#to run the code

linkedList1 = LinkedList()
node1 = Node("A")
linkedList1.append(node1)
node2 = Node("B")
linkedList1.append(node2)
node3 = Node("C")
linkedList1.append(node3)
node4 = Node("D")
linkedList1.append(node4)
linkedList1.deleteNode(2)
linkedList1.printAll()        
'''




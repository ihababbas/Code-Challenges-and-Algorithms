class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None
        
class LinkedList:
     def __init__(self):
        self.head = None
        self.all = []
        
    
     def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    
    
     def printList(self):
         list =[]
         node = self.head
         while node:
            list.append(node.data)
            node = node.next
         
         self.all = list
         print(list)
    
    
     def printMiddle(self):
         count = 0
         mid = self.head
         heads = self.head 
         while(heads != None):
              if count&1:
                mid = mid.next
              count += 1
              heads = heads.next
         if mid!=None:
            print("The middle element is ", mid.data)
            mid_num = int(count / 2)
            print(self.all[mid_num:count])    
             
            


if __name__=='__main__':
     llist = LinkedList()
     
     for i in range(6, 0, -1):
        llist.push(i)
        llist.printList()
        llist.printMiddle()
       

     '''
     llist.push(5)
     llist.push(4)
     llist.push(3)
     llist.push(2)
     llist.push(1)
     llist.printList()
     llist.printMiddle()
       '''
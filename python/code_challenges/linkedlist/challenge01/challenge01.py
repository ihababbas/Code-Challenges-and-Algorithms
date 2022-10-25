class Node:
    def __init__(self, value):
      self.value = value
      self.next = None


class LinkedList():
  def __init__(self):
    self.head=None

  def append(self,node):
    if self.head is None:
      self.head=node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next=node  

  def __str__(self):
    output=""
    if self.head is None : 
      output = "Empty linked list"
    else :
      current=self.head
      while current : 
        output+=f'{current.value}-->'
        current=current.next
      output+= "None"
    return output



def delete_node(node):
  temp = node.next
  node.next = temp.next
  node.value = temp.value
  temp.next = None
  
if __name__=="__main__":
  ll = LinkedList()
  a=Node(3)
  b=Node(5)
  c=Node(9)
  ll.append(a)
  ll.append(b)
  ll.append(c)
  delete_node(b)
  print(ll)

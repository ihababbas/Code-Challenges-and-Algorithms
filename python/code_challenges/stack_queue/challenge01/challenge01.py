# Write here the code challenge solution
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if not self.stack1:
            self.front = x
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        ans = self.stack2.pop()
        
        return ans

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack2:
            return self.stack2[-1]
        
        return self.front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.stack1 and not self.stack2)
  


stack1 = MyQueue()
print(stack1.empty())
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1.peek())
print(stack1.pop())
print(stack1.peek())
print(stack1.empty())
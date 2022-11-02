# Write here the code challenge solution
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.front = None
        

    def push(self, x):
        """
        Push element x to the stack
        :type x: str
        """
        open_list = ["[","{","("]
        close_list = ["]","}",")"]
        for i in x:
            if i in open_list:
                self.stack1.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((len(self.stack1) > 0) and
                      (open_list[pos] == self.stack1[len(self.stack1)-1])):
                    self.stack1.pop()
                else:
                    return "Unbalanced"
        if len(x) == 0:
            self.stack1.append(0)
    
    def output(self):
        """
        Returns the stack of it on right order
        :rtype: bool
        """    
        return True if not self.stack1 else False
   
            


stack1 = MyQueue()
stack1.push("(((())))")

print(stack1.output())


stack2 = MyQueue()
stack2.push("[({}]")
print(stack2.output())

stack2 = MyQueue()
stack2.push("[(hi){}]")
print(stack2.output())

stack2 = MyQueue()
stack2.push("")
print(stack2.output())
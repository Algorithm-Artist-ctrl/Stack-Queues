" Stack using python built in mathod"
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        return self.stack.append(value)
    def pop(self):
        if (len(self.stack)==0):
            print("Stack is empty")
        else:
            return self.stack.pop()
    def peak(self):
        print(self.stack[-1])
    def isempty(self):
        if (len(self.stack)==0):
            print("True")
        else:
            print("False") 
    def size(self):
        print(len(self.stack))
    def traverse(self):
        print(self.stack[::-1])
s=Stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.traverse()
s.pop()
s.traverse()
s.pop()
s.traverse()
s.peak()
s.isempty()
s.size()


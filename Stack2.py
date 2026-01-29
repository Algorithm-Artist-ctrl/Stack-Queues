"Stack using Linked list"
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack():
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top==None
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
    def peak(self):
        if self.isempty():
            return "Stack is Empty"
        else:
            return self.top.data,"Peak Element"
    def pop(self):
        if self.isempty():
            return "Stack is Empty"
        else:
            self.top=self.top.next
    def traverse(self):
        temp=self.top
        while(temp!=None):
            print(temp.data)
            temp=temp.next
s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.traverse()
'''print(s.isempty())
s.traverse()
s.pop()
s.pop()
s.traverse()'''
print(s.peak())
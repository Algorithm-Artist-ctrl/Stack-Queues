class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        return self.top is None
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    def peek(self):
        if self.isempty():
            return "Stack is Empty"
        return self.top.data
    def pop(self):
        if self.isempty():
            return "Stack is Empty"
        popped_value = self.top.data
        self.top = self.top.next
        return popped_value
    def traverse(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next
def reverse_string(text):
    s = Stack()
    for ch in text:
        s.push(ch)
    res = ""
    while not s.isempty():
        res += s.pop()
    print(f"Reverse string: {res}")
reverse_string("hello")

"Queue using Linked list"
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def isempty(self):
        if self.front==None and self.rear==None:
            return "True"
        else:
            return "False"
    def enqueue(self,value):
        new_node=Node(value)
        if self.front==None and self.rear==None:
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
    def dequeue(self):
        if self.front==None and self.rear==None:
            return "Queue is empty"
        else:
            self.front=self.front.next
    def traverse(self):
        temp=self.front
        while temp!=None:
            print(temp.data,end=",")
            temp=temp.next
    def size(self):
        temp=self.front
        count=0
        while temp!=None :
            count=count+1
            temp=temp.next
        return f"size of Queue {count}"
q=Queue()
print(q.isempty())
print(q.traverse())
q.dequeue()
print(q.traverse())
print(q.size())
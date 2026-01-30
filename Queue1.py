class Queue:
    def __init__(self):
        self.__queue = []
    def isempty(self):
        if len(self.__queue) == 0:
            print(True)
        else:
            print(False)
    def enqueue(self, value):
        self.__queue.append(value)
    def dequeue(self):
        if len(self.__queue) == 0:
            print("Queue is empty")
        else:
            return self.__queue.pop(0)
    def size(self):
        count = 0
        for i in self.__queue:
            print(i, end=' ')
            count += 1
        print("\nsize of Queue is", count)
q = Queue()
q.isempty()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.size()
q.dequeue()
q.size()

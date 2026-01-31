class NGE:
    def __init__(self, arr):
        self.arr = arr
        self.num = [-1] * len(arr)
    def next_greater_element(self):
        stack = []
        for i in range(len(self.arr)):
            while stack and self.arr[i] < self.arr[stack[-1]]:
                idx = stack.pop()
                self.num[idx] = self.arr[i]
            stack.append(i)
        return self.num
arr = [4, 5, 2, 25]
nge = NGE(arr)
print(nge.next_greater_element())

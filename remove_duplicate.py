def remove_consecutive_duplicates(arr):
    stack = []

    for item in arr:
        if not stack or stack[-1] != item:
            stack.append(item)

    return stack

arr = [1, 1, 2, 2, 2, 3, 1, 1, 4]
result = remove_consecutive_duplicates(arr)
print(result)

def insertAtEnd(arr, sizeOfArray, element):
    if sizeOfArray > len(arr):
        arr = arr + [element]
        print(*arr, sep=' ')

sizeOfArray = 7
arr = [16,61,47,54,97,57]
element = 30
insertAtEnd(arr, sizeOfArray, element)



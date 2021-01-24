# searching in an unordered list is also called linear search
# iterating over list so performance is O(n)

items = [4, 56, 2, 9, 21, 19, 7]

def finditem(item, list):
    for i in range(0, len(list)):
        if item == list[i]:
            return i
    return None

print(finditem(21, items))

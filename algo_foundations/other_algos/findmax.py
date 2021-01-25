# use a recursive algo to find a maximum value

items = [5, 23, 4, 12, 7, 89, 45, 3, 6]

def find_max(items):
    if len(items) == 1:
        return items[0]
    
    op1 = items[0]
    #print(op1)
    op2 = find_max(items[1:])
    #print(op2)
    if op1 > op2:
        return op1
    else:
        return op2
    
print(find_max(items))


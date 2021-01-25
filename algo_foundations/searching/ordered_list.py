# For an ordered (sorted) list we can use binary search
# Go to the midpoint of the list and check if that value is greater or smaller than the value we look for
# If smaller, repeat the process with the right half of the list, if greater with the left half
# and so on until we find the point equal to the value
# This is O(logn)

items = [6, 8, 19, 23, 48, 51, 62, 68, 91]

def binary_search(item, itemlist):
    listsize = len(itemlist) - 1
    loweridx = 0
    upperidx = listsize

    while loweridx <= upperidx:
        #calculate midpoint
        midpt = (loweridx + upperidx) // 2
        #if thats the item, return it
        if itemlist[midpt] == item:
            return midpt
        
        if item > itemlist[midpt]:
            loweridx = midpt+1
        else:
            upperidx = midpt-1
    
    if loweridx > upperidx:
        return None

print(binary_search(11, items))

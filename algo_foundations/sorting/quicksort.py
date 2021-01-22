#quicksort works like this: select a pivot point, in this case: pick first element as pivot (can be implemented in different ways);
# partition the array so that all the elements less than the pivot are on the left half, and all elements larger are on the right
# recursively repeat this

# quicksort is also divide and conquer like mergesort, has a WORSE case of O(n2) but an average case of O(nlogn) with a constant smaller than mergesort so usually performs better. It's sort-in-place. 

def quicksort(dataset, first, last):
    if first < last:
        #calculate split point
        pivotIdx = partition(dataset, first, last)
        #sort two partitions
        quicksort(dataset, first, pivotIdx-1)
        quicksort(dataset, pivotIdx+1, last)
    
def partition(datavalues, first, last):
    #choose first item as pivot value
    pivotvalue = datavalues[first]
    #establish upper and lower indices
    lower = first + 1
    upper = last
    #start searching for crossing point
    done = False
    while not done:
        #advance lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1
        #advance upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -=1
        #where indices cross, we found split point
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp
    #when split point is found, exchange pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp
    # return split point
    return upper

items = [13, 27, 7, 2, 1, 8, 5, 3]
quicksort(items, 0, len(items)-1)
print(items)



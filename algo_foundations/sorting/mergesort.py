# In mergesort, we break the list down in halfs, until only single elements remain, then we merge all the halfs in a sorted way.
# Turns out that this has O(n log n) so better than bubble sort

def mergesort(dataset):
    if len(dataset)>1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]
        #recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        i=0 #index of left array
        j=0 #index of right array
        k=0 #index of merged array

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i+=1
            else:
                dataset[k] = rightarr[j]
                j+=1
            k+=1
        # at the end maybe left half still has items, move them:
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            k +=1
            i+=1
        # or maybe the right half still has items, move them:
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            k +=1
            j+=1

items = [12, 4, 1, 8, 3, 5, 2, 7]

mergesort(items)
print(items)

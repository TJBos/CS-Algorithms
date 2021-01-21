# Bubble sort is simple sorting algo.
# Go through entire list, compare each item with 1 item over, if first item is larger than swap it. At the end of this, the largest item is at the end (it will 'bubble through' to the end)
# Go through entire list again, up until the second last item, now the the 2 last items are in place.
# Do this over and over (each time the then largest item will bubble to the end) until you're at the beginning of the list
# => you can see perfomance is O(n2)

def bubbleSort(dataset):
    for i in range(len(dataset)-1, 0, -1):
        for j in range(i):
            if (dataset[j] > dataset[j+1]):
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
        #see result of it going through list each time
        #print(dataset)

bubbleSort([5, 12, 4, 2, 3])


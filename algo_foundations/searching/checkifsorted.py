#check if a list is sorted

def issorted(itemlist):
    #you can do this with a for loop but we'll use a python comprehension here
    #in JS similar array method: .every 
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist) -1))



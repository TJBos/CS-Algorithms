#reducing duplicates from a list by turning in a hashtable

items = ["apple", "pear", "banana", "orange", "banana", "grape", "pear"]

filter = dict()

for item in items:
    filter[item] = 0

result = set(filter.keys())

#print(result)

#I think in JS you can just make a Tuple out of an array and convert back to array. Something like this: result = [... new Set(items)]

# -- Value Counting ---
counter = dict()

for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

print(counter)

# in JS we can use reduce to do this as well


#--- Hash Tables ---#
#--------------------#
# Key - Value mapping; each key uniquely points to a value
# most languages have a datatype for this, like dictionary in py and objects in js
# fast lookup times; retrieving value of a known key is O(1)

items = {
    "key1": 1,
    "key2": 2,
    "key3": "three" 
}

items["key4"] = 4

#print(items["key1"])

#iterate over dictionary in python by using items(), do something similar in JS with a for..in loop

for key, value in items.items():
    print(key, value)




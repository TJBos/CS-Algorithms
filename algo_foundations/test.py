class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        print(f'Hello, my name is {self.name}')


bob = Person("Bob", 25)



items = [5, 4, 2, 1]

#def add_two(num):
#   return num + 2

items_added = map(lambda x:x+2, items)

#for item in items_added:
#   print(item)

items_filtered = filter(lambda x: x > 2, items)

for item in items_filtered:
    print(item)


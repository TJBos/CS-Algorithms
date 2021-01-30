class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        print(f'Hello, my name is {self.name}')


bob = Person("Bob", 25)



items = [5, 4, 2, 1]

def add_two(num):
    return num + 2

items_added = map(add_two, items)

for item in items_added:
    print(item)




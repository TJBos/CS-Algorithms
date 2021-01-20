#--- Linked Lists ----
# ---------------------
# Linked lists are really just objects with 2 properties: a data-field and a next-field (pointer)


# Node class

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def get_data(self):
        return self.val
    def set_data(self, val):
        self.val = val
    def get_next(self):
        return self.next
    def set_next(self, next):
        self.next = next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0
    def get_count(self):
        return self.count
    #insert node at the head
    def insert(self, data): 
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1
    #find a node by value
    def find(self, val):
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None
    #delete at index
    def deleteAt(self, idx):
        if idx > self.count-1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx -1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1
    #print content of list
    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and make some nodes
itemList = LinkedList()
itemList.insert(38)
itemList.insert(49)
itemList.insert(13)
itemList.insert(15)
#itemList.dump_list()

#Try the other methods out:
#print(f"Item count: {itemList.get_count()}")
#print(f"Finding item: {itemList.find(13)}")
#print(f"Finding item: {itemList.find(4)}")

itemList.deleteAt(2)
itemList.dump_list()




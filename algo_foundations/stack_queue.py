# --- STACKS ---
# ----------------
# A stack is a series of data with first-in last-out (FILO) order of operations.
# You can PUSH an item on top of the stack and POP it from the top of the stack
# in Python, can be represented with a list (arrays). Adding and removing to/from end of array is O(1).

stack = []

# Adding items to the stack by 'appending', is like push in JS

stack.append(1)
stack.append(2)
stack.append(3)
#print(stack)

# popping items to the stack by 'popping', same in JS

stack.pop()
#print(stack)

# --- QUEUES ---
#---------------
# A queue is a series of data with first-in first-out (FIFO) order of operations.
# you can ENQUEUE an item to the back of the queue, and DEQUEUE an item in the front.
# Can be implemented using lists or arrays BUT is inefficient since adding to front of array is O(n).
# In Python we can use a deque datatype from collections module

from collections import deque
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

#to remove first item added, a deque has a method popleft, in JS similar to array method of shift.
queue.popleft()
print(queue)

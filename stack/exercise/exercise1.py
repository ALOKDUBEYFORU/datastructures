
from Alogirithms.stack.stack import Stack

string1 = 'ALOK'
s1 = Stack()
for i in string1:
    s1.push(i)
print(s1)

curr_node = s1.top
prev_node = None
while curr_node != None:
    next_node  = curr_node.next
    curr_node = prev_node
    prev_node = curr_node
    curr_node = next_node

self.head = prev_node

print(s1)
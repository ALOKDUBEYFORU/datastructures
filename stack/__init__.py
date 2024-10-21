#define Node
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.n = 0

    def size(self):
        return self.n

    def isempty(self):
        return self.top == None

    def push(self,value):
        new_node = Node(value)
        #check whether the stack is empty
        if self.isempty():
            self.top = new_node

        new_node.next = self.top
        self.top = new_node
        self.n = self.n + 1

    def __str__(self):
        if self.isempty():
            return 'stack is empty'
        curr_node = self.top
        sstack = ""
        for i in range(0,self.n):
            sstack = sstack + str(curr_node.data)+"->"
            curr_node = curr_node.next
        return sstack[:-2]

    def pop(self):
        if self.isempty():
            return 'Stack is empty'
        pop_val = self.top.data
        self.top = self.top.next
        self.n = self.n - 1
        return pop_val

    def peek(self):
        if self.isempty():
            return 'stack is empty'

        return self.top.data

if __name__ == "__main__":
    s1 = Stack()
    print(s1)
    print(s1.size())
    s1.push(1)
    s1.push(2)
    s1.push(3)

    print(s1.size())
    print(s1.peek())
    print(s1)
    print(s1.pop())
    print(s1)
    print(s1.pop())
    print(s1)
    print(s1.pop())
    print(s1)

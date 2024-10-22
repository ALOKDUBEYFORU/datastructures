
class Node:
    #constructor definition
    def __init__(self,value):
        '''
        constructor for Node accepts value and initializes three attributes i.e.., Data, prev and next
        '''
        #initialize data with the argument value
        self.data = value
        #initialize the prev attribute with None.
        self.prev = None
        # initialize the next attribute with None.
        self.next = None

class Double_Linked_List:

    def __init__(self):
        '''
        Constructor of Double Linked List class initiates the head, tail and number of elements.
        '''
        #Initialting head attribute to store the address of first node in future.
        self.head = None
        #Initialting tail attribute to store the address of first node in future.
        self.tail = None
        # Initialting number of elements attribute to store the number of elements in future.
        self.n = 0

    def insert_head(self,value):
        '''
        Inserts the Node at head position of Double Linked List. Once the new node had been insrted,
        it becomes the head node.
        '''
        #create a new node with the supplied value
        new_node = Node(value)
        #Check whether Double linked list is empty
        if self.head == None and self.tail == None :
            #assign the newly created node to head
            self.head = new_node
            # assign the newly created node to tail
            self.tail = new_node
        #Double Linked list is not empty.
        else:
            #let us assign the next attribut of new node as the existing head node
            new_node.next = self.head
            # let us assign the previous attribute of current head node with the newly created node
            self.head.prev = new_node
            #make the new node as head
            self.head = new_node
        #increment the number of elements by 1.
        self.n = self.n + 1

    def insert_tail(self,value):
        '''
        insert_tail method will help us in adding the node at a tail position. This newly added
        node will become the new tail.
        '''
        #Let us create a new node with the supplied
        new_node = Node(value)
        #to check whether the Double Linked List is empty
        if self.head == None and self.tail == None :
            #as the Double linked list is empty, add the newly created node as both head and tail.
            self.head = new_node
            self.tail = new_node
        #Doubel linked list is not empty.
        else:
            #store the address of the existing tail at the previous element of new node
            new_node.prev = self.tail
            #assign the address of new_node to existing tail node as next node.
            self.tail.next = new_node
            #new node will be the tail.
            self.tail = new_node
        #increment the number of elements by 1.
        self.n = self.n + 1

    def __str__(self):
        '''
        str function is called, whenever the class variable is called from inside of a print method.
        '''
        #check whether the Double linked list is empty.
        if self.head == None:
            return "double linked list is empty"
        #check whether double linked list has a single item.
        if self.head == self.tail:
            # return the data of single node
            return str(self.head.data)
        #loop through multiple nodes
        curr_node = self.head
        #create a string
        dllstr = ""
        #loop from head node to tail nodes
        while curr_node != self.tail.next:
            #concatenate the nodes
            dllstr = dllstr + str(curr_node.data)+"<-->"
            #navigate to next node
            curr_node = curr_node.next
        #return the string
        return dllstr[:-4]

    def check_index_pos(self,index_pos):
        '''
        To check whether the index position is between 0 and total number of elements.
        '''
        #check whether the index_pos lies between 0 and n.
        if 0<= index_pos < self.n :
            #if it lies, then return True
            return 1
        #return False, if the index is out of range.
        return 0

    def insert_node(self,index_pos,value):
        '''
        insert_node method will be used to create a node with the provided value and insert it
        at the index position
        '''
        #to check whether the index position is a valid one.
        if self.check_index_pos(index_pos):
            #create a new node
            new_node = Node(value)
            #start the traveral from the left to right. Hence, start with the head node.
            curr_node = self.head
            #for tracking the nodes, initiate a counter variable
            i = 0
            #loop till we reach the node prior to the index position
            while i< index_pos - 1:
                #navigate to the next node
                curr_node = curr_node.next
                #increment the counter by one.
                i = i + 1
            #assign the address of new node to the node at index position's previous element
            curr_node.next.prev = new_node
            #assign the address of node at index position to newly created node's next element
            new_node.next = curr_node.next
            new_node.prev = curr_node
            curr_node.next = new_node
            #increment the counter by 1
            self.n = self.n+1
        else:
            print('invalid index position')

    def find_index_value(self,index_pos):
        '''
        find_index_value returns the value at the given index position
        '''
        #check whether the DLL is empty
        if self.head == None:
            return "Double Linkedlist is empty"
        #check whether the index position provided is a valid one.
        if self.check_index_pos(index_pos):
            #start from head
            curr_node = self.head
            #initiate a counter
            i = 0
            #loop through till the index position
            while i < index_pos:
                #navigate to the next node
                curr_node = curr_node.next
                #increment the counter
                i = i + 1
            #return the value at the current node
            return curr_node.data
        else:
            return "Invalid index position"

    def find_value_index(self,value):
        '''
        find_value_index return the index position based on the value provided. It returns the first
        occurance of the value only.
        '''
        #check whether the DLL is empty
        if self.head == None:
            return 'Double linked list is empty'
        #check whether DLL has only one element
        if self.head == self.tail :
            #check whether the element value is same as that of the input value
            if self.head.data == value:
                return 0
            else:
                return "Could not find value"
        #let us loop through the nodes starting from head node.
        curr_node = self.head
        #initiate the index_pos as zero.
        index_pos = 0
        #start the loop
        while curr_node != self.tail.next:
            #compare the value of node with that of the input value
            if curr_node.data == value:
                #return the index position
                return index_pos
            #increment the index poistion by 1.
            index_pos = index_pos + 1
            #go to next node
            curr_node = curr_node.next
        return "Could not find value"

    def pop(self,index_pos=None):
        '''
        pop function is used to delete the element from the DLL.
        '''
        try:
            #check if the index position had not been assigned, then choose the last eleement.
            if index_pos == None:
                index_pos = self.n-1
            #check whether DLL is empty
            if self.head == None:
                return "Double linked list is empty"
            #check whether the head and tail are pointing to a same element.
            if self.head == self.tail:
                #assigning the popping value to a local variable
                pop_value = self.head.data
                #initiate the constructor again
                self.__init__()
                #return the pop value
                return pop_value
            #check whether the index position is the last element of the DLL
            elif index_pos == self.n-1 :
                #move the tail pointer to one node to left.
                curr_node = self.tail
                pop_value = curr_node.data
                curr_node = curr_node.prev
                curr_node.next = None
                self.tail = curr_node
            elif index_pos == 0 :
                #moving the head pointer to one node right
                curr_node = self.head
                pop_value = curr_node.data
                curr_node = curr_node.next
                curr_node.prev = None
                self.head = curr_node

            else:
                #navigate through the loop
                i = 0
                curr_node = self.head
                pop_value = self.find_index_value(index_pos)
                prev_node = self.head
                next_node = self.head
                while i < index_pos:
                    prev_node = curr_node
                    curr_node = curr_node.next
                    next_node = curr_node.next
                    i = i + 1
                print('pooping value',prev_node.data)
                next_node.prev = prev_node
                prev_node.next = next_node
            #decrement the counter by 1.
            self.n = self.n - 1
            print(pop_value)
            return pop_value
        except Exception as e:
            print('exception had reached ',e)

if __name__ == "__main__":
    '''dll1 = Double_Linked_List()
    dll1.insert_head(10)
    dll1.insert_head(20)
    dll1.insert_tail(30)
    dll1.insert_tail(40)
    dll1.insert_node(1,15)
    print('printing the DLL ', dll1)

    #print('value present at index position 2',dll1.find_index_value(2))
    #print('value presnet at 3rd index position', dll1.find_index_value(3))
    #print('value presnet at 0th index position', dll1.find_index_value(0))
    #print('value presnet at 4th index position', dll1.find_index_value(4))
    print('index position of value 15 ',dll1.find_value_index(15))
    print('index position of value 25 ',dll1.find_value_index(25))
    print('index position of value 20 ',dll1.find_value_index(20))
    print('index position of value 40 ',dll1.find_value_index(40))
    print(dll1)'''
    dll2 = Double_Linked_List()
    dll2.insert_head(10)
    dll2.insert_head(20)
    dll2.insert_head(30)
    dll2.insert_head(40)
    print('printing ',dll2)
    print('popping last item',dll2.pop())
    print('printing ',dll2)
    print('popping 1st element',dll2.pop(1))
    print('printing ',dll2)
    print('popping 0th element',dll2.pop(0))
    print('printing ',dll2)
class Node:
    def __init__(self,data):
        '''
        construction of class Node is used to create an instance with two attributes data and next.
        data is used to store the values of the nodes and next is used to store the address of the
        next nodes.
        :param data:
        '''
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        '''
        Constructor of class LinkedList. This method is used to initiate the pointer and counter
        attributes.
        '''
        #Pointer for storing the address of first node or an empty linked list
        self.head = None
        #for storing the count of nodes in the linkedlist
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self,value):
        '''
        Insert_head method is used to create a node with the supplied value and insert it as a head
        node. The counter is incremented to represent that the node had been added.
        :param value:
        :return:
        '''
        #Create a new node
        new_node = Node(value)

        #Assign the value of head to new_node
        new_node.next = self.head

        #As new_node became the first element, let us point the head to the new node
        self.head = new_node

        #As the new node had been created, let us increement of node counter by one.
        self.n = self.n + 1

    def insert_tail(self,value):
        '''
        Insert_tail method is used to insert a node with the supplied value as the node.
        :param value:
        :return:
        '''

        #creation of a new node
        new_node = Node(value)

        #check whether the linked list is empty
        if self.head is None:
            #assign the address of new_node to self.head, as there are no elements exists.
            self.head = new_node
        else:
            #go to first node
            node1 = self.head
            #loop through next nodes.
            for i in range(0,self.n):
                #check whether the next attribute is None.
                if node1.next is None:
                    #assign the address of new node to the existing tail.
                    node1.next = new_node
                #navigate to next node
                node1 = node1.next

        #incremeent the counter value by one
        self.n = self.n + 1

    def insert(self,index_pos,value):
        '''
        Insert function is used to insert a new node at the given index position in the linked list
        :param index_pos:
        :param value:
        :return:
        '''

        #check whether the index position is a valid one.
        if self.index_pos_in_range(index_pos):
            # create a new node
            new_node = Node(value)

            #navigate from head node to the index position
            node1 = self.head
            #navigate till the index position
            for i in range(0,index_pos):
                #check if we are in at an index position less than one.
                if i == index_pos-1:
                    #assign the address of next node to new node
                    new_node.next = node1.next
                    #assign the address of the new node to the node at indes_pos - 1
                    node1.next = new_node
                #navigate to next node
                node1 = node1.next

            #increment variable by one.
            self.n = self.n + 1
        else:
            print('invalid index number')

    def __str__(self):
        '''
        Method used to return the nodes of the linkedlist in the FIFO basis. This is used when
        we use the class instance in the print statement.
        :return:
        '''
        #Define an empty string
        lstr = ""
        #To return the string that Linkedlist is empty, if the linkedlist does not have any elements.
        if self.head is None:
            return "LinkedList is empty"
        #Assign the head node
        node1 = self.head
        #loop through number of nodes.
        for i in range(0,self.n):
            #append the values present in data attribute of Node to the string.
            lstr = lstr+str(node1.data)+"-->"
            #go to next node
            node1 = node1.next

        #return the string excluding last three characters.
        return lstr[:-3]

    def index_pos_in_range(self,index_pos):
        '''
        To check whether the index position provided is a valid one i.e.., it lies between 0 and the
        maximum number of nodes.
        :param index_pos:
        :return:
        '''
        if 0<=index_pos<self.n :
            return 1
        return 0

    def __getitem__(self,index_pos):
        '''
        getitem member is used to return the value present at any given index position.
        :param index_pos:
        :return:
        '''

        #To check whether the index position is a valid one.
        if self.index_pos_in_range(index_pos):
            # Assign the first node to the node1 variable
            node1 = self.head

            #Navigate through the linked list
            for i in range(0,index_pos+1):
                #check whether the index position had been reached,
                if i == index_pos:
                    #return the value of the node
                    return node1.data
                #go to next node
                node1 = node1.next
        #since the index position is out of range, return an error.
        return "Invalid Index"

    def index(self,value):
        '''
        Index method returns the index position of the first node in which the supplied value exists.
        :param value:
        :return:
        '''

        #go to first node of the linked list
        node1 = self.head
        #loop through all of the nodes
        for i in range(0,self.n):
            #check whether the value of node matches with the value provided
            if node1.data == value:
                #return the index position
                return i
            #go to next node
            node1 = node1.next
        #searched value could not be found.
        return 'value not found in the linked list'

    def pop(self,index_pos=None):
        '''
        pop method is used to delete an item based on the index position
        :param index_pos:
        :return:
        '''

        #Check if the index position had been kept as blank.
        if index_pos is None:
            #assign the last element.
            index_pos = self.n-1

        #To check whether the index position is a valid one
        if self.index_pos_in_range(index_pos):
            #go to first node
            node1 = self.head
            #check whether we need to pop the head node
            if index_pos == 0 :
                #assign the next node as head node by assigning the next node's address to head pointer
                self.head = node1.next
                #fetch the element value of first node
                return_val =  node1.data
            #if the index position is either in the range or last index position.
            for i in range(0,index_pos):
                #check whether we would like to pop the last element.
                if i == index_pos - 1 == self.n - 2:
                    #fetch the element value of last item
                    return_val = node1.next.data
                    #assign the node1.next as None. Thus by making it as a tail node.
                    node1.next = None
                #check whether we at a node previous to node that needs to he deleted.
                elif i == index_pos-1:
                    #Fetch the value of the node that is going to be deleted.
                    return_val = node1.next.data
                    #assign the address stored in the node, that is going to be deleted, to the node
                    # present at one step behind node
                    node1.next = node1.next.next
                #navigate to next node
                node1 = node1.next
            #decrement the counter by one.
            self.n = self.n - 1
            #return the value of the popped node
            return return_val
        else:
            print('Invalid index position')

    def remove(self,value):
        '''
        remove method is used to remove the first node found based on the value.
        :param value:
        :return:
        '''
        #go to first node
        node1 = self.head
        #check whether the value matches with that of the value in the head node
        if node1.data == value:
            #let us move the head pointer to the second node
            self.head = node1.next
            #decrement the counter by 1.
            self.n = self.n-1
            #return the value
            return
        #loop thorugh all the nodes.
        for i in range(0,self.n-1):
            #Check whether vale of next node matches with that of value.
            if node1.next.data == value:
                #assign the node's next's next element to the existing node's next.
                node1.next = node1.next.next
                #decrement the counter by one.
                self.n = self.n-1
                #go back to main program.
                return
            #go to next node
            node1 = node1.next
        #print the error message, if the value is not found in linked list
        print('value could not be found')

    def extend(self,l2):
        '''
        extend method allows us to add the elements from the other linked list as well.
        :param l2:
        :return:
        '''
        #if both the linked lists are empty, then do nothing
        if self.head == l2.head == None:
            return
        #if the linkedlist being passed is empty, then do nothing
        if l2.head == None:
            return

        #check if existing linked list is empty.
        if self.head == None:
            #assign the head of the linked list passed to the current node
            self.head = l2.head
            #change the value of the existing linked list by the counter of passed linked list.
            self.n = l2.n
            return

        #navigate to the last element of current list.
        node1 = self.head
        #loop through the all the elements.
        for i in range(0,self.n):
            #Check whether the node is the last element
            if i == self.n-1:
                #assign the head of the second linked list to the current list's address.
                node1.next = l2.head
                #increase the size counter by the counter of l2 as well.
                self.n = self.n+l2.n
            #go to next node
            node1 = node1.next

if __name__ == "__main__":
    #Instantiate the linkedlist
    l = LinkedList()
    #To check the length of the newly created linkedlist
    print('length of linkedlist after creating the empty linked list',len(l))
    #to create a new node
    l.insert_head(1)
    l.insert_head(2)
    # To check the length of the newly created linkedlist
    print('length after inserting two nodes',len(l))
    print('Displaying linked list l :',l)
    print('Displying 0th element of the list :',l[0])
    print('Displying 1st element of the list :', l[1])
    print('Displying 2nd element of the list :', l[2])
    print('Displying index position of value 1 in the linkedlist :', l.index(1))
    print('Displying index position of value 2 in the linkedlist :', l.index(2))
    print('Displying index position of value 3 in the linkedlist :', l.index(3))
    print('adding a node with value 3 at tail node',l.insert_tail(3))
    print('adding a node with value 4 at tail node', l.insert_tail(4))
    print('Displaying linked list after adding the tail nodes :', l)
    print('adding a node with value 10 at index 1 ', l.insert(1,10))
    print('adding a node with value 11 at index 6', l.insert(6,11))
    print('Displaying linked list after inserting in the middle of nodes :', l)
    print('popping a node at index 1', l.pop(1))
    print('popping a node at the last index', l.pop())
    print('popping a node at the 0th index', l.pop(0))
    print('popping a node at the 10th index', l.pop(10))
    print('Displaying linked list after inserting in the middle of nodes :', l)
    print('removing value 1 from linkedlist',l.remove(1))
    print('removing value 2 from linkedlist',l.remove(2))
    print('removing value 4 from linkedlist', l.remove(4))
    print('removing value 10 from linkedlist', l.remove(10))
    print('Displaying linked list after removing the elements :', l)
    # Instantiate the linkedlist
    l1 = LinkedList()
    # To check the length of the newly created linkedlist
    print('length of linkedlist after creating the empty linked list',len(l))

    # to create a new node
    l1.insert_head(3)
    l1.insert_head(4)
    # To check the length of the newly created linkedlist
    print('length after inserting two nodes',len(l))
    print('Displaying linked list l1 :', l1)
    print('extending the l by l1 :',l.extend(l1))
    print('new list : ',l)
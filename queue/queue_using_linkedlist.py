class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        '''
        enqueue method adds the new node to the queue from tail end or rear side.
        '''
        #create a new node
        new_node = Node(value)
        #check whether the rear node points to any of the node
        if self.is_empty():
            #if rear does not points to any of the node, then the newly created node will acts as both
            #front and rear nodes.
            self.front = new_node
            self.rear = new_node
        #Queue has elements
        else:
            #start with the rear node
            curr_node = self.rear
            #assign the new node to the next attribute of rear.
            self.rear.next = new_node
            #make the new node as the rear node.
            self.rear = new_node

    def is_empty(self):
        '''
        is_empty method is used to check whether the queue is empty.
        '''
        #returns True, if the queue is empty or else would return False.
        return self.front == None


    def __str__(self):
        '''
        __str__ method is used to display the nodes in a sequential manner starting from front to rear.
        '''
        #Verify whether the Queue is empty.
        if self.is_empty():
            return 'Queue is empty'
        #Queue has the elements.
        else:
            #start from front node.
            curr_node = self.front
            #initiate a string
            qstr = ""
            #loop through till we reach rear.
            while (curr_node!= self.rear.next):
                #append the values to the string.
                qstr = qstr + str(curr_node.data) + "<-"
                #navigate to the next node
                curr_node = curr_node.next
            #return the string
            return qstr[:-2]

    def dequeue(self):
        '''
        dequeue method helps us in removing a node from Queue.
        '''
        #verify whether the Queue is empty
        if self.is_empty():
            return "None to Dequeue"
        #Queue has elements
        else:
            #navigate to front node
            curr_node = self.front
            #move front node to the next node.
            self.front = curr_node.next

    def size(self):
        '''
        size method helps us to count the nodes in the queue.
        '''
        #check whether the queue is empty
        if self.is_empty():
            return 0
        #go to front node
        curr_node = self.front
        #initiate the counter variable
        counter = 0
        #navigate till the end of the queue
        while curr_node != self.rear.next:
            #increment the counter by 1
            counter = counter + 1
            #navigate to the next node
            curr_node = curr_node.next
        #return the counter variable
        return counter

    def front_value(self):
        '''
        front_value method is used to display the value present in the front node
        '''
        #Verify whether the queue has elements.
        if self.is_empty():
            return "Queue is empty"
        #if the queue has elements
        else:
            #return the data in the front node.
            return self.front.data

    def rear_value(self):
        '''
        rear_value method is used to return the value present in the rear node.
        '''
        #verify whether the Queue is empty
        if self.is_empty():
            return "Queue is empty"
        #if the Queue has elements
        else:
            #return the value from rear node.
            return self.rear.data


if __name__ == "__main__":
    queue1 = Queue()
    print('printing queue',queue1)
    print('whether the queue is empty ? ', queue1.is_empty())
    print('enqueuing value 10',queue1.enqueue(10))
    print('enqueuing value 20',queue1.enqueue(20))
    print('enqueuing value 30',queue1.enqueue(30))
    print('enqueuing value 40',queue1.enqueue(40))
    print('printing queue1 ',queue1)
    print('dequeue an node',queue1.dequeue())
    print('queue after dequeue',queue1)
    print('dequeue an node',queue1.dequeue())
    print('queue after dequeue',queue1)
    print('displaying the size',queue1.size())
    print('displaying the value from front node',queue1.front_value())
    print('displaying the value from second node',queue1.rear_value())
    print('verifying whether queue is empty',queue1.is_empty())
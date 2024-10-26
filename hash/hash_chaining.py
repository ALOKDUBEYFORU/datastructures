class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.llsize = 0

    def append(self,key,value):
        new_node = Node(key,value)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.llsize = self.llsize + 1

    def __setitem__(self,key,value):
        self.append(key,value)
    def __str__(self):
        if self.head == None:
            dstr = 'Linked List is empty'
        else:
            curr_node = self.head
            dstr = ""
            while curr_node != self.tail.next:
                dstr = dstr + str(curr_node.key)+':'+str(curr_node.value)+"<-->"
                curr_node = curr_node.next
        return dstr

    def index(self,key):
        if self.head != None:
            curr_node = self.head
            counter = 0
            while curr_node != self.tail.next:
                if curr_node.key == key:
                    return counter
                curr_node = curr_node.next
                counter = counter + 1
        return -1

    def get_node_at_index(self,index_pos):
        temp = self.head
        counter = 0
        while temp != None:
            if counter == index_pos:
                return temp
            temp = temp.next
            counter = counter + 1

    def ll_remove(self,key):
        if self.head != None:
            curr_node = self.head
            if curr_node.key == key:
                self.head = self.head.next
                return 'deleted'

            while curr_node != self.tail:
                if curr_node.next == self.tail and curr_node.next.key == key:
                    curr_node.next = None
                    self.tail = curr_node
                    return 'deleted'

                if curr_node.next.key == key :
                    curr_node.next = curr_node.next.next
                    return 'deleted'
                curr_node = curr_node.next
        return 'key not found'


    def len(self):
        return self.llsize


class Dictionary:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.dictelements = 0
        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):
        L = []
        for i in range(capacity):
            L.append(LinkedList())
        return L

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def rehash(self, capacity):
        # create a temporary bucket of the size capacity

        old_buckets = self.buckets

        self.buckets = self.make_array(capacity * 2)
        self.capacity = capacity * 2
        self.dictelements = 0
        for i in range(len(old_buckets)):
            for node in range(old_buckets[i].len()):
                if old_buckets[i].get_node_at_index(node) != None:
                    self.put(old_buckets[i].get_node_at_index(node).key, old_buckets[i].get_node_at_index(node).value)

    def get_node_index(self, bucket_index, key):
        node_index = self.buckets[bucket_index].index(key)
        return node_index

    def put(self, key, value):
        '''
        put method is used to insert or update a key in a bucket.
        '''
        # let us calculate the load factor.
        load_factor = self.dictelements / self.capacity
        # If the load_factor is above 2.
        if load_factor >= 2:
            # use the rehashing for the same.
            self.rehash(self.capacity)

        # get the index of the key based on the hash function.
        bucket_index = self.hash_function(key)
        # search for the index of the node in that particular bucket.
        node_index = self.get_node_index(bucket_index, key)

        # Verify whether the key does not exists.
        if node_index == -1:
            # append the key and value
            self.buckets[bucket_index].append(key, value)
            # As we are trying to insert the value, let us increase the value.
            self.dictelements = self.dictelements + 1
        # index had been found for the key.
        else:
            # let us get the address of the node.
            node = self.buckets[bucket_index].get_node_at_index(node_index)
            # update the value of an existing string.
            node.value = value

    def __str__(self):
        '''
        str method is used to display the contents of the buckets.
        '''
        # create a new empty string
        dstr = ""
        # let us loop through bucket in buckets.
        for i in range(self.capacity):
            # loop through each bucket.
            dstr = dstr[:-4] + "\n" + 'bucket-' + str(i) + "->"
            # let us add the linked list to the string
            dstr = dstr + str(self.buckets[i]) + '<-->'
        return dstr[:-4]

    def get(self, key):
        '''
        get method is used to display the indices of bucket and node
        for a particular key.
        '''

        if self.dictelements > 0:
            # loop through the number of buckets in the buckets
            for i in range(self.capacity):
                # loop through nodes in the bucket
                for j in range(self.buckets[i].len()):
                    # Verify whether any of the key of an existing node matches
                    # with that of given key.
                    if self.buckets[i].get_node_at_index(j).key == key:
                        return 'found in bucket ' + str(i) + ' at node - ' + str(j)

        # return the no element exists message.
        return "No elements exists"

    def remove(self, key):
        '''
        to remove a key from the buckets.
        '''

        # check if the we have more than 1 dict eleements
        if self.dictelements > 0:
            # loop through each bucket in buckets
            for i in range(self.capacity):
                # to delete the key
                is_deleted = self.buckets[i].ll_remove(key)
                # if deleted from any of the bucket, the return.
                if is_deleted == 'deleted':
                    return 'deleted'
        # declare that the key was not found
        return 'key not found'




if __name__ == "__main__":
    dict1 = Dictionary()
    print('inserting Python with a value of 40',dict1.put('python',40))
    print('inserting c with a value of 400',dict1.put('c', 400))
    print('inserting c++ with a value of 500',dict1.put('c++',500))
    print('inserting java with a value of 600',dict1.put('java', 600))
    print('printing dictionary after insertions',dict1)
    print('insert of update the value of key python with 50',dict1.put('python', 50))
    print('printing dictionary after insertion/updation of key python',dict1)
    print('print the value of the key python',dict1.get('python'))
    print('delete the key python',dict1.remove('python'))
    print('printing dictionary after removal of string python',dict1)
    print('delete the key c',dict1.remove('c'))
    print('printing dictionary after removal of string c',dict1)
    print('delete the key php', dict1.remove('php'))
    print('printing dictionary after removal of string php', dict1)

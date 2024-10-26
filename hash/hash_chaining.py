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
    def __init__(self,capacity=2):
        self.capacity = capacity
        self.dictelements = 0
        self.buckets = self.make_array(self.capacity)

    def make_array(self,capacity):
        L = []
        for i in range(capacity):
            L.append(LinkedList())
        return L

    def hash_function(self,key):
        return abs(hash(key))%self.capacity

    def rehash(self,capacity):
        #create a temporary bucket of the size capacity

        old_buckets = self.buckets

        self.buckets = self.make_array(capacity * 2)
        self.capacity = capacity * 2
        self.dictelements = 0
        for i in range(len(old_buckets)):
            for node in range(old_buckets[i].len()):
                if old_buckets[i].get_node_at_index(node) != None:
                    self.put(old_buckets[i].get_node_at_index(node).key,old_buckets[i].get_node_at_index(node).value)

    def get_node_index(self,bucket_index,key):
        node_index = self.buckets[bucket_index].index(key)
        return node_index

    def put(self,key,value):
        bucket_index = self.hash_function(key)
        self.dictelements = self.dictelements + 1

        #let us calculate the load factor.
        load_factor = self.dictelements / self.capacity

        if load_factor >= 2 :
            self.rehash(self.capacity)

        node_index = self.get_node_index(bucket_index,key)

        if node_index == -1:
            self.buckets[bucket_index].append(key,value)
        else:
            node = self.buckets[bucket_index].get_node_at_index(node_index)
            node.value = value


    def __str__(self):
        dstr = ""
        for i in range(self.capacity):
            dstr = dstr[:-4] +"\n"+ 'bucket-'+str(i) + "->"
            if self.buckets[i] != None :
                dstr = dstr + str(self.buckets[i])+'<-->'
        return dstr[:-4]

    def get(self,key):
        if self.dictelements > 0 :
            for i in range(self.capacity):
                for j in range(self.buckets[i].len()):
                    if self.buckets[i].get_node_at_index(j).key == key:
                        return 'found in bucket '+str(i)+' at node - '+str(j)
        return "No elements exists"

    def remove(self,key):
        if self.dictelements >0 :
            for i in range(self.capacity):
                is_deleted = self.buckets[i].ll_remove(key)
                print(is_deleted)
                if is_deleted == 'deleted':
                    return 'deleted'
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

class Dictionary:
    '''Dictionary class is similar to dict class in python and is being implemented using the
    linear probing technique in hashing'''
    incremental_factor = 2
    def __init__(self,size=1):
        self.size = size
        self.key_list = [None] * self.size
        self.value_list = [None] * self.size
        self.n = 0

    def hash_function(self,key):
        '''
        hash_function method is used to generate the index position of the array.
        '''
        return abs(hash(key))%self.size

    def resize(self,capacity):
        '''
        resize method is used to increase the size of the array with the given capacity.
        '''
        #Create a temporary list with the capacity
        temp_key_list = [None] * capacity
        temp_value_list = [None] * capacity

        #copy the elements from the existing list.
        for i in range(0,len(self.key_list)):
            temp_key_list[i] = self.key_list[i]
            temp_value_list[i] = self.value_list[i]

        #creation of keylist
        self.key_list = [None] * capacity
        self.value_list = [None] * capacity
        self.size = capacity
        self.n = 0
        #assign the temporary list to the original list by rehashing it.
        for i in range(0,len(temp_key_list)):
            if temp_key_list[i] != None:
                self.put(temp_key_list[i],temp_value_list[i])


    def rehash(self,old_hash):
        return (old_hash+1)%self.size

    def put(self,key,value):
        '''
        put method is used to insert the key value pair in the Dictionary class.
        The following algorithm needs to be followed.
        If the dictionary contains no free elements,
            resize the dictionary

        generate the index position using the hash_function.
        if the index position is empty
            add the key value in that index position
        else
            if the existing key with the new key. if it is a match
                update the value
            else
                generate a new hash key by rehashing
                loop to be continued till we either find None value or the key element.
                    if None is found
                        add the key,value pair
                    else if key is found then
                        update the value.
                    generate a new hash value by rehashing
        '''
        if self.size == self.n:
            self.resize(self.n*Dictionary.incremental_factor)

        hash_val = self.hash_function(key)

        if self.key_list[hash_val] == None:
            self.key_list[hash_val] = key
            self.value_list[hash_val] = value
        else:
            if self.key_list[hash_val] == key:
                self.value_list[hash_val] = value
            else:
                new_hash_value = self.rehash(hash_val)
                while True:
                    if self.key_list[new_hash_value]== None:
                        self.key_list[new_hash_value] = key
                        self.value_list[new_hash_value] = value
                        break
                    elif self.key_list[new_hash_value] == key:
                        self.value_list[new_hash_value] = value
                        break
                    new_hash_value = self.rehash(new_hash_value)
        self.n = self.n + 1

    def __setitem__(self,key,value):
        self.put(key,value)

    def __str__(self):
        dstr = " "
        for i in range(0,len(self.key_list)):
            if self.key_list[i] != None :
                dstr = dstr+str(self.key_list[i])+":"+str(self.value_list[i])+' '
        return dstr

    def get(self,key):
        hash_value = self.hash_function(key)
        if self.key_list[hash_value] == key:
            return self.value_list[hash_value]
        else:
            current_pos = hash_value
            counter = 0
            rehash_value = self.rehash(hash_value)
            while counter< len(self.key_list):
                if self.key_list[rehash_value] == key :
                    return self.value_list[rehash_value]
                elif self.key_list[rehash_value] == None:
                    return "Value not found"
                rehash_value = self.rehash(rehash_value)
                counter = counter+1

            return 'Value not found'

    def __getitem__(self, key):
        return self.get(key)

if __name__ == "__main__":
    d1 = Dictionary()
    d1['python'] = 45
    d1['java'] = 50
    d1['c'] = 100
    print(d1)
    print(d1['python'])
    print(d1['java'])
    print(d1['c'])
    print(d1['python+'])
    d1['c++'] = 1000
    d1['php'] = 2500
    print(d1)
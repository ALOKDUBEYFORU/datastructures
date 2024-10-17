# Let us create our own array data type.
#ctypes is a foreign function library to python. It provides the C compatible data types.
import ctypes


def create_array(capacity):
    #creating a new array of size capacity
    new_array = (capacity*ctypes.py_object)()
    #return the instance of the above array
    return new_array


class MyArray:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = create_array(self.size)

    def append(self,item_value):

        if self.size == self.n:
            self.create_copy_array(self.size*2)

        self.A[self.n] = item_value
        self.n = self.n+1

    def create_copy_array(self,capacity):
        #creation of a blank array with the size capacity
        B = create_array(capacity)

        #copying the data from A to B
        for i in range(0,len(self.A)):
            B[i] = self.A[i]

        #Assign B to A.
        self.A = B
        self.size = capacity

    def __str__(self):
        disp_str = ''

        for i in range(0,self.n):
            disp_str = disp_str+str(self.A[i])+","

        return '['+disp_str[:-1]+']'

    def check_item_in_range(self,index_pos):
        if 0 <= item < self.n or -1>=item>=-self.n:
            return 1
        return 0

    def __getitem__(self, item):
        if check_item_in_range(item):
            return self.A[item]
        else:
            raise IndexError('list index out of range')

    def __len__(self):
        return self.n

    def pop(self,item = None):
        if item is None:
            item = self.n-1
        item_val = self.A[item]
        #Create a new array of size self.A
        B = create_array(self.size)
        #if the item had been assigned a  +ve value
        if check_item_in_range(item):

            if item >= 0:
                j = 0
                for i in range(0,self.n):
                    if i != item:
                        B[j] = self.A[i]
                        j = j+1
                self.A = B
                self.n = self.n-1
            else:
                pass
if __name__ == "__main__":
    try:
        arr1 = MyArray()
        arr1.append(3.11)
        arr1.append(True)
        arr1.append('Hello')
        arr1.append(3.12)
        print(arr1)
        print(len(arr1))
        print(arr1.pop(1))
        print(arr1)

    except Exception as e:
        print(e)


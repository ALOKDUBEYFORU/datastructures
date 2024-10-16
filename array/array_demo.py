# Let us create our own array data type.
#ctypes is a foreign function library to python. It provides the C compatible data types.
import ctypes

class MyArray:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.create_array(self.size)

    def create_array(self,capacity):
        #creating a new array of size capacity
        new_array = capacity*ctypes.py_object
        #return the instance of the above array
        return new_array()

    def append(self,item_value):

        if self.size == self.n:
            self.create_copy_array(self.size*2)

        self.A[self.n] = item_value
        self.n = self.n+1

    def create_copy_array(self,capacity):
        #creation of a blank array with the size capacity
        B = self.create_array(capacity)

        #copying the data from A to B
        for i in range(0,len(self.A)):
            B[i] = self.A[i]

        #Assign B to A.
        self.A = B

    def __str__(self):
        disp_str = ''

        for i in self.A:
            disp_str = disp_str+str(i)+","

        return '['+disp_str[:-1]+']'


if __name__ == "__main__":
    arr1 = MyArray()
    arr1.append(4)
    print(arr1.n,arr1.size)
    arr1.append(True)
    print(arr1.n, arr1.size)
    arr1.append('Hello')
    print(arr1.n, arr1.size)
    arr1.append(3.12)
    print(arr1.n, arr1.size)
    print(arr1)
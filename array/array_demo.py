
# Let us create our own array data type.
#ctypes is a foreign function library to python. It provides the C compatible data types.
import ctypes

def create_array(capacity):
    try:
        #creating a new array of size capacity and create the instance of this class
        new_array = (capacity*ctypes.py_object)()
        #return the instance of the above class
        return new_array
    except Exception as e:
        print('Error in create array')

class MyArray:
    #Defining a class variable for storing the increment_factor
    increment_factor = 2
    def __init__(self):
        '''
        variables :
            size :  to keep track of total size of the array
            n : to keep track of the number of elements in the array
        functionality :
            To initialize the two variables i.e.., size and n. To create an array of size 1.
        '''

        self.size = 1
        self.n = 0
        self.A = create_array(self.size)

    def append(self,item_value):
        '''
        This method accepts the item_value and appends it to the end of the array. Prior to adding the
        item, it checks whether number of elements are equal to the size of the array. If they are same,
        then resizes the array to the double of size.
        :param item_value:
        :return:
        '''
        try:
            if self.size == self.n:
                self.create_copy_big_array(self.size*MyArray.increment_factor)
            self.A[self.n] = item_value
            self.n = self.n + 1
        except Exception as e :
            print('exception in append')

    def create_copy_big_array(self,capacity):
        '''
        This method creates a new array of size capacity. It copies the elements of the arrays from
        the old array to new array. It assigns the new array to old array. Thus it resizes the old array.
        :param capacity:
        :return:
        '''
        try:

            #creation of a blank array with the size capacity
            B = create_array(capacity)

            #copying the data from A to B
            for i in range(0,len(self.A)):
                B[i] = self.A[i]

            #Assign elements of B to A.
            self.A = B
            self.size = capacity
        except Exception as e:
            print('Exception in create_copy_big_array')

    def __str__(self):
        '''
        This method is used to display the array elements. It loops through all the elements of the
        array and concatenate them to the string and returns this string.
        :return:
        '''
        try:

            disp_str = ''

            for i in range(0,self.n):
                disp_str = disp_str+str(self.A[i])+","

            return '['+disp_str[:-1]+']'
        except Exception as e:
            print('Exception raised for the str method',e)
    def check_item_in_range(self,index_pos):
        '''
        This method checks whether the index position passed to the method is within the range.
        :param index_pos:
        :return:
        '''
        try:

            if (0 <= index_pos < self.n) or (-1 >= index_pos >= -1 * self.n):
                return 1
            return 0
        except Exception as e:
            print('exception raised in check_item_in_range',e)
    def __getitem__(self, index_pos):
        '''
        This method returns the value of the item after checking whether this index position exists
        in range.
        :param Index_pos:
        :return: The value present at index_pos position in the array
        '''
        try:
            if check_item_in_range(index_pos):
                return self.A[index_pos]
            else:
                raise IndexError('list index out of range')
        except Exception as e:
            print('Exception in getitem',e)
    def __len__(self):
        '''
        This method returns the len of the array.
        :return: n
        '''
        return self.n

    def pop(self,index_pos = None):
        '''
        This method is used to accept the index_position. It removes the item value and returns the value.
        :param index_pos: Optioanl arguement. If not yet passed, then it will consider the last element.
        :return: value at index_pos
        '''
        if index_pos is None:
            index_pos = self.n-1
        if self.check_item_in_range(index_pos):
            item_val = self.A[index_pos]
            #starting from the pop element prepare a loop and move the element towards the pop element.
            if index_pos >= 0 :
                starting_point = index_pos
            elif index_pos < 0:
                starting_point = self.n + index_pos
            for i in range(starting_point,self.n-1):
                self.A[i] = self.A[i+1]

            self.n = self.n-1

            return item_val
        else:
            raise IndexError('list index out of range')

    def clear(self):
        '''
        Reinitiate the array to it's initial state.
        :return:
        '''
        self.__init__()

    def index(self,item_val):
        '''
        This method accepts the item value and returns the index position in the array.
        :param item_val: Item value
        :return: index position of the item value
        '''
        try:
            for i in range(0,self.n):
                if self.A[i] == item_val:
                    return i
            return -1
        except Exception as e:
            print("exception raised in index",e)
    def insert(self,index_pos,item_val):
        '''
        This method is used to insert a value at the given index position. If the array is full, then it
        resizes as well.
        :param index_pos:
        :param item_val:
        :return:
        '''
        try:
            if self.check_item_in_range(index_pos) :

                if self.size == self.n:
                    self.create_copy_big_array(self.size * MyArray.increment_factor)

                if index_pos > 0:
                    ending_point = index_pos
                elif index_pos <0:
                    ending_point = self.n + index_pos
                elif index_pos == 0 :
                    ending_point = 1

                for i in range(self.n,ending_point,-1):
                    self.A[i] = self.A[i-1]
                self.A[index_pos] = item_val
                self.n = self.n + 1
        except Exception as e:
            print('exception raised in insert block',e)


    def remove(self, item_val):
        '''removes the first element based on the value provided'''
        #Use the find method to get the index position of the value.
        index_pos = self.index(item_val)
        if index_pos is not None:
            for i in range(index_pos,self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n-1
        else:
            print('Unable to find the value in the array to remove')

    def __delitem__(self,index_pos):
        if index_pos is not None:
            a1 = self.pop(index_pos)


if __name__ == "__main__":
    try:
        arr1 = MyArray()
        arr1.append(3.11)
        arr1.append(True)
        arr1.append('Hello')
        arr1.append(3.12)
        print(arr1)
        print(len(arr1))
        print('popping up -1 element',arr1.pop(-1))
        print(arr1)
        print('popping up 2 element', arr1.pop(2))
        print(arr1)
        print('inserting 2 value at 1st index',arr1.insert(1,2))
        print('Array after insertion',arr1)
        print('inserting 3 value at 2nd index', arr1.insert(2, 3))
        print('Array after insertion', arr1)
        print('remove element 2 from arr1',arr1.remove(2))
        print('Array after removal', arr1)
        print('remove element 2 from arr1', arr1.remove(1.12))
        print('Array after removal', arr1)
    except Exception as e:
        print(e)


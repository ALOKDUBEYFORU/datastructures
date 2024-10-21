# Let us create our own array data type.
#ctypes is a foreign function library to python. It provides the C compatible data types.
import ctypes

def create_stack(capacity):
    try:
        #creating a new stack of size capacity and create the instance of this class
        new_stack = (capacity*ctypes.py_object)
        #return the instance of the above class
        return new_stack()
    except Exception as e:
        print('Error in creating a stack')

class MyStack:
    '''
    MyStack class is used to create a stack using the implementation of arrays.
    This class has the following members.
    1. push :
    2. pop :
    3. peek :
    4. size :
    5. isempty :
    '''

    #define the increment factor
    increment_factor = 2

    #define the constructor
    def __init__(self):
        #To initiate the size of the stack to 1.
        self.size = 1
        #To initiate the size of stack to zero, as the stack is empty.
        self.top = 0
        #To create a stack with the size 1.
        self.StackA = create_stack(self.size)

    def resize_stack(self,increment_factor):
        '''
        resize_stack is used to create a new stack of the multiple of increment factor of the original array and copy the existing elements
        of the stack into new stack and return the newly created stack.
        :param increment_factor:
        :return:
        '''
        #Create an empty stack of increment_factor size.
        StackB = create_stack(increment_factor)

        #loop through the elements of the existing stack
        for i in range(0,self.top):
            #assigning the stack elements from old stack to new stack.
            StackB[i] = self.StackA[i]

        #Increase the size of the stack to increment_factor
        self.size = increment_factor

        #return the new stack.
        return StackB


    def push(self,value):
        #To verify whether the stack is full.
        if self.size == self.top :
            #If the stack is full, then resize the stack by the increment_factor times of existing size
            self.StackA = self.resize_stack(self.size*MyStack.increment_factor)

        #assign the value to the last element of the stack.
        self.StackA[self.top] = value

        #To increase the size of stack by one.
        self.top = self.top + 1

    def __str__(self):
        #To check whether the stack is empty.
        if self.is_empty() :
            #If the stack is empty, the return the message that stack is empty.
            return "Stack is empty"

        #Initialize the stack by "".
        sstr = ""
        #loop through the elements of the stack
        for i in range(0,self.top):
            #append the stack elements to the string.
            sstr = sstr + str(self.StackA[i])+ "<-"

        #return the string except last two characters.
        return sstr[:-2]

    def is_empty(self):
        #To check whether the number of elements in the stack is zero.
        if self.top == 0 :
            #if the stack has no elements, then return 1.
            return 1
        #if the stack has more elements, then retuen zero.
        return 0

    def pop(self):
        #To veridfy whethe the stack is empty.
        if self.is_empty():
            return "Stack is empty"
        #To retrieve the value of the Top
        pop_value = self.StackA[self.top-1]
        #reduce the value of n to n-1
        self.top = self.top-1
        #return the popped value.
        return pop_value

    def peek(self):
        '''
        peek method is used to return the value of the element at top.
        :return:
        '''

        #To verify whether the stack is empty.
        if self.is_empty():
            return 'Stack is empty'

        #To return the value of last eement
        return self.StackA[self.top-1]

if __name__ == "__main__":

    s1 = MyStack()
    print(s1)
    print('Let us push three values (10,20,30) in to the stack')
    s1.push(10)
    s1.push(20)
    s1.push(30)
    print('displaying the stack values after pushing three values',s1)
    print('popping one value',s1.pop())
    print('displaying the stack values after popping a value', s1)
    print('displaying the peek value',s1.peek())
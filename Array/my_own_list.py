import ctypes

class myList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # create a c tpye array of size = self.size
        self.myArray = self.__create_Array(self.size)
    
    def __create_Array(self, capacity):
        # creates a c type array ( static, refrential) with size capacity
        return (capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n == self.size:
            # resize
            self.__resize(self.size*2)
        # APPEND
        self.myArray[self.n] = item
        self.n = self.n + 1

    def __resize(self, new_capacity):
        # create a new array with new capacity
        myResizedArray = self.__create_Array(new_capacity)
        self.size = new_capacity
        # copy the element from myArray to myResizedArray
        for i in range(self.n):
            myResizedArray[i] = self.myArray[i]
        # reassign myArray
        self.myArray = myResizedArray

    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.myArray[i]) + ','
        return '[' + result[:-1] + ']'
    
    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.myArray[index]
        else:
            raise IndexError('index not in range')
        
    def pop(self):
        if self.n == 0:
            return 'Empty List'
        print(self.myArray[self.n - 1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):
        for i in range(self.n):
            if self.myArray[i] == item:
                return i
        return 'valueError not in list'
    
    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        for i in range(self.n, pos, -1):
            self.myArray[i] = self.myArray[i-1]
        
        self.myArray[pos] = item
        self.n = self.n + 1

    def __delitem__(self, pos):
        if 0 <= pos < self.n:
            for i in range(pos, self.n -1):
                self.myArray[i] = self.myArray[i+1]
            self.n = self.n - 1
    
    def remove(self, item):
        pos = self.find(item)
        if type(pos) == int:
            #delete
            self.__delitem__(pos)
        else:
            return pos
        
    def merge(self, anotherList):
        for i in anotherList:
            self.append(i)
    
    # def sort(self):
    #     min = 0
    #     for i in range(self.n):
    #         if min> i



test = myList()
# print(type(test))
# print(test)
test.append('hello')
test.append(1)
test.append(True)
test.append('hii')


# print(len(test))

# print('initial array',test)
# test.pop()
# print('on poping array',test)
# test.clear()
# print('on clearing array',test)
# test.pop()
# print('on popping again',test)

# print(test.find('30'))

# print(test)
# test.insert(0,'inserted')
# print(test)

# print(test)
# del test[0]
# print(test)

test2 = myList()
test2.append(1)
test2.append(2)
test2.append(3)
test2.append(4)

test.merge(test2)

print(test)
# test.remove(1)
# print(test)
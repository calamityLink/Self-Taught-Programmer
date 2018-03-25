##class Data:
##    def __init__(self):
##        self.nums=[1,2,3,4,5]
##
##    def change_data(self,index,n):
##        self.nums[index]=n
##
##data_one = Data()
##data_one.nums[0]=100
##print(data_one.nums)
##
##data_two = Data()
##data_two.change_data(0,100)
##print(data_two.nums)

##class PublicPrivateExample:
##    def __init__(self):
##        self.public = 'safe'
##        self._unsafe = 'unsafe'
##
##    def public_method(self):
##        #safe for the client to call this
##
##    def _unsafe_method(self):
##        #not safe for the client to call this

##print(type('Hello, world!'))
##print(type(200))
##print(type(200.1))
##print(type(['A','B','C']))
##print(type(('A','B','C')))
##print(type({'job':'programmer',
##            'home':'house',
##            'pets':'two cats'}))

##class Shape():
##    def __init__(self,w,l):
##        self.width = w
##        self.len = l
##
##    def print_size(self):
##        print('{} by {}'.format(self.width,self.len))
##
##class Square(Shape):
##    def __init__(self,w):
##        self.width = w
##    
##    def area(self):
##        return self.width**2
##
##    def print_size(self):
##        print('I am a {} by {} square'.format(self.width,self.width))
##              
##
##my_square = Square(25)
##my_square.print_size()
##print(my_square.area())

##class Dog():
##    def __init__(self,n,b,o):
##        self.name = n
##        self.breed = b
##        self.owner = o
##
##class Person():
##    def __init__(self,n):
##        self.name = n
##
##mick = Person("Mick Jagger")
##stan = Dog('Stanley','Bulldog',mick)
##print(stan.owner.name)

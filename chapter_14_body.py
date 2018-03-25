##class Rectangle():
##    rect_list = []
##
##    def __init__(self,w,l):
##        self.width = w
##        self.length = l
##        self.rect_list.append((self.width,self.length))
##
##    def print_size(self):
##        print('{} by {}'.format(self.width,self.length))
##
##r1 = Rectangle(10,24)
##r2 = Rectangle(20,40)
##r3 = Rectangle(100,200)
##
##print(Rectangle.rect_list)


##class Lion:
##    def __init__(self,n):
##        self.name = n
##
##    def __repr__(self):
##        return self.name
##
##lion = Lion('Dilbert')
##print(lion)


##class AlwaysPositive:
##    def __init__(self,n):
##        self.n = n
##
##    def __add__(self,other):
##        return abs(self.n + other.n)
##
##x = AlwaysPositive(10)
##y = AlwaysPositive(-20)
##
##print(x+y)


##class Person:
##    def __init__(self):
##        self.name = 'Bob'
##
##bob = Person()
##same_bob = bob
##print(bob is same_bob)
##
##another_bob = Person()
##print(bob is another_bob)
##
##bob.name = 'Bobby'
##print(bob.name)
##print(same_bob.name)
##print(bob is same_bob)


##x = 10
##if x is None:
##    print('x is None :(')
##else:
##    print('x is not None')
##
##x = None
##if x is None:
##    print('x is None')
##else:
##    print('x is not None :(')

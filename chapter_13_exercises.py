##Exercises 1 to 3
##
##class Shape:
##    def what_am_i(self):
##        print('I am a shape!')
##
##class Rectangle(Shape):
##    def __init__(self,w,l):
##        self.width = w
##        self.length = l
##
##    def perimeter(self):
##        return self.width * 2 + self.length * 2
##
##class Square(Rectangle):
##    def __init__(self,w):
##        self.width = w
##
##    def perimeter(self):
##        return self.width * 4
##
##    def change_size(self,i):
##        if i < -self.width:
##            self.width = 0
##        else:
##            self.width += i
##
##my_rect = Rectangle(10,20)
##my_square = Square(10)
##
##print(my_rect.perimeter())
##print(my_square.perimeter())
##
##my_square.change_size(-2)
##print(my_square.perimeter())
##
##my_rect.what_am_i()
##my_square.what_am_i()


##Exercise 4
##
##class Rider:
##    def __init__(self,n):
##        self.name = n
##
##class Horse:
##    def __init__(self,n,c,r):
##        self.name = n
##        self.color = c
##        self.rider = r
##
##my_rider = Rider('Link')
##my_horse = Horse('Babby','cow-spotted',my_rider)
##
##print(my_horse.rider.name)

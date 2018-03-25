##Exercises 1 to 3
##
def obj_compare(x,y):
    if x is y:
        print('{} is {}'.format(x,y))
    else:
        print('{} is not {}'.format(x,y))

class Square:
    sq_list = []
    
    def __init__(self,w):
        self.width = w
        Square.sq_list.append(self.width)
        print('A new square has been created that is {} by {} by {} by {}'.format(self.width,self.width,self.width,self.width))

    def __repr__(self):
        return('Square with width {}'.format(self.width))

sq1 = Square(10)
sq2 = Square(15)
sq3 = sq1

print(Square.sq_list)
obj_compare(sq1,sq2)
obj_compare(sq1,sq3)

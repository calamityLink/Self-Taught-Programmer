##def f(x):
##    return x+1
##
##z = f(4)
##
##if z == 5:
##    print("z is 5")
##else:
##    print("z is not 5")
##
##
##def g(x,y,z):
##    return x+y+z
##
##result = g(1,2,3)
##print(result)
##
##
##def make_none():
##    butts = 1 + 2
##
##none_result = make_none()
##print(none_result)
##
##
##age = input("Enter your age: ")
##int_age = int(age)
##if int_age < 21:
##    print("You are young!")
##else:
##    print("Wow, you are old!")
##    
##
##def even_odd(x):
##    if x%2 == 0:
##        print("even")
##    else:
##        print("odd")
##
##even_odd(2)
####even_odd(3)
##
##def even_odd2():
##    n = input("Type a whole number: ")
##    n = int(n)
##    if n%2 == 0:
##        print("That is even")
##    else:
##        print("That is odd")
##
##even_odd2()
##even_odd2()
##
##
##
##def add_it(x,y=10):
##    return x+y
##
##result = add_it(2)
##print(result)
##result = add_it(2,3)
##print(result)
##
##def f(x):
##    x=1
##    y=2
##    z=3
##
##print(x)  #these three lines will generate error due to local scope of x, y, and z
##print(y)
##print(z)
##
##
##x = 100
##
##def f():
##    """
##    Adds 1 to the
##    variable x
##    """
##    global x
##    x +=1
##    print(x)
##
##f()
##
##
##
##a = input("type a number:")
##b = input("type another:")
##
##try:
##    a = int(a)
##    b = int(b)
##    print(a/b)
##except(ZeroDivisionError, ValueError):
##    print("Invalid input.")






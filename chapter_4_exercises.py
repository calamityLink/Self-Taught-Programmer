print("Exercise 1")

def f(x):
    """
    Returns the input squared
    :param x: int
    :return: x squared
    """
    return x**2

in_var = int(input("Type a number: "))
print(f(in_var))


print("Exercise 2")
print("")
def f(x):
    """
    Simply prints the input
    :param x: string
    :no return:
    """
    print(x)

in_string = input("Type anything: ")
f(in_string)


print("Exercise 3")
def f(x,y,z,a=1,b=2):
    """
    Takes the base score, adds and subtracts bonuses and penalties, and applies optional multipler and exponent.
    :param x: int (base score)
    :param y: int (penalties)
    :param z: int (bonuses)
    :param a: optional int (multiplier)
    :param b: optional int (exponent)
    :return: int result of ((base score - penalties + bonuses) * multiplier) raised to the exponent.
    """
    return ((x - y + z) * 1 )**b

print("Let's do some math!")
x_in = int(input("Enter a starting score: "))
y_in = int(input("Enter the penalties: "))
z_in = int(input("Enter the bonuses: "))

score = f(x_in, y_in, z_in)


print("The final score is...")
print(score)


print("Exercise 4")
def divider(x):
    """
    Divides the input by 2.
    :param x: int
    :return: int x divided by 2
    """
    return x/2

def multer(y):
    """
    Multiplies the input by 4.
    :param y: int
    :return: int y times 4.
    """
    return y*4

result = divider(10)
print(multer(result))


print("Exercise 5")
def f(x):   
    """
    Tries to convert the input to a float. Will complain if invalid input.
    :param x: string
    :return: None
    """
    try:
        y = float(x)
        print("Thanks!")
    except ValueError:
        print("Invalid input")

float_in = input("Give me a decimal number: ")
f(float_in)


##print("Exercise 6 is adding docstrings to the above functions")

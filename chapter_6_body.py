my_string = """line one
              line two
              line three"""
print("The string is " + my_string)

author = "Kafka"

print(author[0])
print(author[4])

long_string = "We'll try doing a negative index with the end of this stringz!"
print(long_string)
print(long_string[-2])

print("cat " + "in " + "the " + "hat")
print("butts"*3)

noun = "boy"
verb = "done farted"
adjective = "under"
noun2 = "bridge"

print("The {} {} {} the {}".format(noun,verb,adjective,noun2))
      
print("Hello.Yes.Oh my!".split("."))

print(" *pfft* ".join(["The","fox","jumped"]))

print("     Too many spaces     ".strip())

print("Normal string".replace("o","0"))

print("animals".index("m"))

try:
    print("animals".index("z"))
except:
    print("z is not in \"animals\"")

print("Cat" in "Cat in the Hat")
print("Bat" not in "Cat in the Hate")

print("You do not need to escape 'single quotes' within double quotes.")
print('You do not need to escape "double quotes" within single quotes, either.')

print('line1\nline2\nline3')

fict = ["Tolstoy","Camus","Orwell","Huxley","Austin"]
print(fict[1:3])

ivan = "In place of death there was light."
print(ivan[0:17])
print(ivan[17:34])
print(ivan[:17])
print(ivan[17:])

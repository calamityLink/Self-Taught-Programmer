##Exercise 1
##
##for show in ['The Walking Dead','Entourage','The Sopranos','The Vampire Diaries']:
##    print(show)

##Exercise 2
##
##for i in range(25,51):
##    print(i)

##Exercise 3
##
##shows = ['The Walking Dead','Entourage','The Sopranos','The Vampire Diaries']
##for i in range(0,4):
##    print(str(i+1) + ". " + shows[i])

##Exercise 4
##
##notrandom = 1
##while True:
##    response = input("Guess a number from 1 to 5 or type n to quit: ")
##    if response == 'n':
##        break
##    elif int(response) in range(1,6):
##        if int(response) == notrandom:
##            print("Congrats! You guessed correctly!")
##        else:
##            print("Sorry! The number was {}".format(notrandom))
##    else:
##        print('Invalid input!')
##    notrandom = (notrandom + 2) % 5 + 1

##Exercise 5
##
##list1 = [8,19,148,4]
##list2 = [9,1,33,83]
##multed = []
##
##for item1 in list1:
##    for item2 in list2:
##        multed.append(item1*item2)
##
##print(multed)

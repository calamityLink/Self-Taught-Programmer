##for character in "Ted":
##    print(character)
##
##for show in ['GOT','Narcos','Vice']:
##    print(show)
##
##for show2 in ["A. Development","Friends","Always Sunny"]:
##    print(show2)
##
##people = {"G. Bluth II":'A. Development',
##          "Barney":'HIMYM',
##          'Dennis':'Always Sunny'}
##
##for character2 in people:
##    print(character2)
##
##tv = ['GOT','Narcos','Vice']
##i = 0
##for show3 in tv:
##    tv_upper = tv[i].upper()
##    tv[i] = tv_upper
##    i+=1
##print(tv)
##
##tv2 = ['GOT','Narcos','Vice']
##for j, show4 in enumerate(tv2):
##    tv_upper2 = tv2[j].upper()
##    tv2[j] = tv_upper2
##print(tv2)
##
##tvn = ['GOT','Narcos','Vice']
##coms = ['Arrested Development','Friends','Always Sunny']
##all_shows = []
##
##for shown in tvn:
##    shown = shown.upper()
##    all_shows.append(shown)
##
##for shown2 in coms:
##    shown2 = shown2.upper()
##    all_shows.append(shown2)
##
##print(all_shows)
##
##for k in range(1,11):
##    print(k)
##
##x = 10
##while x > 0:
##    print('{}'.format(x))
##    x-=1
##print('Happy New Year!')
##
##qs = ['What is your name?\n',
##      'What is your fav. color?\n',
##      'What is your quest?\n']
##
##n = 0
##while True:
##    print('Type q to quit')
##    a = input(qs[n])
##    if a == 'q':
##        break
##    n = (n+1)%3
##
##for i in range(1,6):
##    if i ==3:
##        continue
##    print(i)
##
##j = 1
##while j<=5:
##    if j == 3:
##        j+=1
##        continue
##    print(j)
##    j+=1
##
##for i in range(1,3):
##    print(i)
##    for letter in ['a','b','c']:
##        print(letter)
##        
##list1 = [1,2,3,4]
##list2 = [5,6,7,8]
##added = []
##for i in list1:
##    for j in list2:
##        added.append('{} + {} = {}'.format(i,j,i+j))
##print(added)
##
##while input('y or n?') != 'n':
##    for i in range(1,6):
##        print(i)
##        

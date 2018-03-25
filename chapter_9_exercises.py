##import os
##
##filepath = os.path.join('C:',os.sep,'Users','Colin','Documents','TestForPython.txt')
##with open(filepath,'r') as f:
##    print(f.read())


##userinput = input('Type a word to save: ')
##with open('Chap9Exercise2.txt','w') as f:
##    f.write(userinput)


import csv

movie_list = [['Top Gun','Risky Business','Minority Report'],
              ['Titanic','The Revenant','Inception'],
              ['Training Day','Man on Fire','Flight']]

with open('Chap9Exercise3.csv','w',newline='') as f:
    r = csv.writer(f,delimiter=',')
    for sublist in movie_list:
        r.writerow(sublist)

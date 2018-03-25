##import os
##print(os.path.join('Users','bob','st.txt'))
##
##st = open('st.txt','w')
##st.write('Hi from Python!')
##st.close()
##

##with open('st.txt','w') as f:
##    f.write('Hi from Python! 2')

##with open('st.txt','r') as f:
##    print(f.read())

##my_list = list()
##
##with open('st.txt','r') as f:
##    my_list.append(f.read())
##
##print(my_list)

##import csv
##
##with open('st.csv','w',newline='') as f:
##    w = csv.writer(f,delimiter=',')
##    w.writerow(['one','two','three'])
##    w.writerow(['four','five','six'])

import csv

with open('st.csv','r') as f:
    r = csv.reader(f,delimiter=',')
    for row in r:
        ##print(','.join(row))
        print(row)


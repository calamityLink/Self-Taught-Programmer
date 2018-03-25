##import re
##
##l = 'Beautiful is better than ugly.'
##matches = re.findall('beautiful',l,re.IGNORECASE)
##print(matches)

##import re
##string = "Two too."
##m = re.findall('t[ow]o',string,re.IGNORECASE)
##print(m)

##import re
##line = '123?34 hello?'
##m = re.findall('\d',line,re.IGNORECASE)
##print(m)

##import re
##line = '__one__ __two__ __three__'
##m1 = re.findall('__.*__',line,re.IGNORECASE)
##print(m1)
##m2 = re.findall('__.*?__',line,re.IGNORECASE)
##print(m2)

##import re
##
##text = '''Giraffes have aroused the curiousity of __PLURAL_NOUN__ 
##since earliest times. The giraffe is the tallest of all 
##living __PLURAL_NOUN__, but scientists are unable to explain 
##how it got its long __PART_OF_THE_BODY__. The giraffe's 
##tremendous height, which might reach __NUMBER__ __PLURAL_NOUN__, 
##comes from its legs and __BODYPART__.'''
##
##def mad_libs(mls):
##    '''
##    :param mls: String with parts the user should fill out
##    surrounded by double underscores. Underscores cannot be
##    inside hint e.g., no __hint_hint__ only __hint__.'''
##
##    hints = re.findall('__.*?__',mls)
##
##    if hints is not None:
##        for word in hints:
##            q = 'Enter a {}'.format(word)
##            new = input(q)
##            mls = mls.replace(word,new,1)
##        print('\n')
##        mls = mls.replace('\n','')
##        print(mls)
##    else:
##        print('invalid mls')
##
##mad_libs(text)

import re

line = 'I love $'
m = re.findall('\\$',line,re.IGNORECASE)
print(m)

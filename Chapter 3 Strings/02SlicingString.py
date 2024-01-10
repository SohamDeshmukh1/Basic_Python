'''Slicing and joining strings in python'''#(LEARNED)

a = "Hello "
b = "GamerzWorld"

#print(a+b) (in this the strings get )
c = a+b
# this is the second way u can do it
print(c)
print("After putting index 0 the output")
print(b[0])

'''About [] '''
# [] will be used to enter the index number
# And the index will be used to show the content
# on that index number 

'''SLICING PART'''
#print(b[0:6])
#print(b[:6]) # this will also work as b[0:6]
print(b[0:]) # this will work as b[0:11] we have to index+1 at the 
print(b[-5:])# this works as b[6:11]
print(b[6:11])# in this the indexs is 0 and 10 BUT U KNOW THE LOGIC SOS STOPP
# last part[0:_]for the empty portion
# BASICIALLY U KNOW WHAT U HAV TO DO

''' Explaination'''
# this is called slicing
# The value inside the index box is the limit
# or it tell only this many content of index
#should be printed
"""RULE"""
# Rule : 0 will be included and 6 will not be included
# it wont count the index 6 it will stop at 5
# ":" is used to tell the range betwwen 2 index
''''Trick or Just a guess'''
# or on human hand the 6 can be counted as number 
# of letters which u wants to print from 0
'''' Different Types of list '''
''' 6 types learned
.sort
.reverse
.remove
.pop
.insert
.append - Most used and Important'''

#Note-\n does not works in lists too SED ;-;
l = [1,4,26,24,3,10,9,22,30]
# dont forget to put [] or else it will be a string
# not a list
l.sort()#1 sorts the list
print(l)

l = [1,4,26,24,3,10,9,22,30,]
#as list changes itself so copied the above list
l.reverse()#2 reverses the list
print(l)

l = [1,4,26,24,3,10,9,22,30]
l.append(26) #3 Appends at the end of list
# the data inside bracket will be inserted at the 
# end of the list
print(l)

l = [1,4,26,24,3,10,9,22,30]
l.insert(1,26)#4 Inserts the number at the given index
# and changes the position or the index of other data
print(l)

l = [1,4,26,24,3,10,9,22,30]
l.pop(0)#5 Removes the data at the given index
print(l)

l = [1,4,26,24,3,10,9,22,30]
l[0]= 99
l.remove(4)#6 Works same as pop but does not need index
# this function uses The exact data to get removed
print(l)

# UPDATE - LIST VALUES CAN BE CHANGES EXTERNALLY
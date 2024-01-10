# Got to learn that a string can also be replace
# to use the string functions
letter = '''\nDear user
you are selected 

 the  is date |date|'''
user = input("Enter Your name:\n")
date = input ("Enter the date:\n")
letter = letter.replace("user",user)
letter = letter.replace("|date|",date)

print(letter)
#Added a bit perfection or presentation in short ;-;
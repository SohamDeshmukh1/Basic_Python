# Arithamatic operators(LEARNED)
a = 2
b = 8
#print("The addition is ",a+b,"of a and b")
#in above line learned to put an calculated value between sentence

#arthmetic Operators 
print("The addition is =",a+b) # or can be written ",2+8
print("The subtraction is =",a-b)
print("the division is =",a/b)
print("the multiplication is =", a*b)

# Assignment operators(LEARNED)
c = 12
print(c)
c += 2
print(c)
c -= 2
print(c)          # in this operation the value of c changes and 
c *= 2            # gets overwrite as using only 1 variable and
print(c)          # and many assignmnets operator at same time 
c /= 2            # U know what happened so dont worry u learned it 
print(c)

# Comparision Operators(LEARNED)
# d = (14>7)        
# d = (14<7)        # these signs are know as relational operators in C
# d = (14>=7)       # booyent is an datatype as pyhton has 5 of them            
# d = (14<=7)       # booyent is returned which automaticaly tells
# d = (14==7)       # if the statement is true or not  
d = (14!=7)         # in the operation tell
print(d) #uncomment the code lines to see if it works
        
# Logicial Operators(Partialy learned as Different forusing conditions)
'''In python logicial Operators does not have Symbols like &&,||,!
they directly uses and,or,not as its an high level language'''
b = False #Logicial Operators works on boolyent maths 
a = True # Or we can say on true and false
print("The value of a and b is equal =",(a and b))
print("The value of a and b is different =",(a or b))
print("The value of b is ", (not b))
print("The value of a is ", (not a))
"""                       STRING FUNCTIONS                                """

story = '''soham is just learning a skill
known as coding so he can make anything he
desire and may earn respect for it'''

#Just an lame sentence which is an string
#To get the length of an string

'''String Function'''

print(len(story))#(1) len
print(story.endswith("it"))#(2) .endswith
print(story.count("e"))#(3) .count
print(story.capitalize())#(4).capitalize
print(story.find("soham"))#(5).find
#note find will only show the word once when it founded the word at start
#then even if there is 2 times use it will only show 1 output is shown in index number
print(story.replace("soham","Sumeet"))#(6).replace 

#(LEARNED)
# the length of the string also counts the space
# given between the words or data

#(LEARNED)
#story is the name of variable
#.endswith is the function to tell wether the 
# string ends with data given to crosscheck
#in the bracket("(text/data)") we have to input data
# The output is given in the form of boolyent

#(LEARNED)
#This function counts the occurance of an character
#Basicially ye check karta hai ke abhi 
#bracket mai e dala hai to string story mai kete
#bar e aya hai ye vo function count karke batayega
#also insted of "e" even we can put words or number

#(LEARNED)
#this function will make the first word of first letter capital
# in the string u may run and check it

#(LEARNED)
#This function will only tell if there is the specific words 
#availiable in the string with index
#if the word is not availiable the index output shown will be
#an negative index

#(learned)
#in replace function it works as .replace("oldword","NewWord")
#in output which will be displayed





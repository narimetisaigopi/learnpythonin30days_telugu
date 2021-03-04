# Python 2.7.16
# intro this session
# 1) indentation
# 2) Comments
# 3) variable and its rules
# 4) Type Casting


print("Hello world")

#indentation
if 0 > 1 :
    print("yes it is correct")
    n = 0
else:
    print("i am out")
    print("i am out2")

#comments
a = 9
b = 3
print(a+b) # this will add both the numbers

#print("i will be off")

# multiline comments
'''
Python 2.7.16
intro this session
1) indentation
2) Comments
3) variable and its rules
4) Type Casting
'''

#variables in python
name = "Sai Gopi"
myName = 'Sai Gopi' # string
#age = 25

# variables case sensitive
name = "Sai Gopi"
Name = "Narimeti"


myStory = '''
this is my normal story
thank you
happy coding
'''

print(myStory)
print(Name)

myCollegeName = "Vigan college" # camel case
my_college_name = "Vigan college" # snake case


''''
1) starts with alphabets or _
2) not strats with number
3) A-Z or a-z or 0-9 or _
'''

# type casting 
data = "23"
print(type(data))
age = int("23") # str,bool
print(type(age))
print(age)

















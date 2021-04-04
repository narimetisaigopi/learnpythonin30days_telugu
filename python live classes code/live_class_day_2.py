# https://docs.google.com/document/d/1yNynjoF9-yZy60peTOwovhug6nFGkR2o6R-WyroT7gY/edit
# Data types
# list []
# tuple ()
# set {}
 

marks = 20 #int
price = 134.563434444444444444444 # float
com = -56.3e10 # complex

sasa = float(marks)
convertedPrice = int(price)

print(convertedPrice)

name = "Sai Gopi"
name2 = 'Sai Gopi'

name2 = '''
Sai Gopi
sasa
sa
s
asa
'''

myAge = "25"

print(int(myAge) - 5)

name = "Sai Gopi"
name2 = "Vicky"

# List
names = ["Gopi","Sai","Vicky","Honey"] # hertogeneuos 
        #  0      1      2      3     4  index
''' 
    []
mutable (changable)
unordered
Duplicates 
'''
names.append("Sai")
names.remove("Gopi")
# pop()
# sort
# insert
print(names)

#Tuples
frds = ("Sai","Gopi","Lucky")
''' 
    ()
immutable (unchangable)
ordered
Duplicates 
sorting
'''
print(names.sort())

#set
students = {"Sai","Gopi","Sai",2,True}
''' 
{}
immutable (unchangable)
unordered
No Duplicates 
'''
print(len(students))

# dict

myData = {"name":"Sai Gopi","name":"Sai Gopi2","age":25,"activeUser":True}
ags = myData['age']
myData["age"] = 28

myData["bio"] = "Good"

''' 
{"key":"hey"}
mutable 
unordered 3.6 
ordered 3.7
No Duplicates keys
'''
print(myData)

isPass = False
isFail = True

#range
print(10>90)
mslist = range(90,100,2)
for n in mslist:
    print(n)


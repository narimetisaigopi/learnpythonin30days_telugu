# Scope and iterabale
# Global keyboard

'''
Scopes (India)
1) Local Scope (Telangana)
2) Global Scope (Pan India)
'''

name = "Hyderbad" #Global
def getMyCity():
    name = "Madhira" #Local
    print("my city is "+name)
    def post(): # inner functions
        print("post is "+name)
    post()
    
getMyCity()

# global keyboard

gender = "Male"

def myFunc():
   global age # local scope global variable
   age = "25"
   global gender
   gender = "Female"

myFunc()
print("Age is: "+age)


#iterators
names = ["Siva","Ganesh","Ramu"]
# for name in names:
#     print("Name is "+name)

namesIterator = iter(names) # converts to iterable object

# next() method using for traversing the iterable object

#__iter__():
#__next__():

print("using iterator >>> "+next(namesIterator))  # names[0] 
print("using iterator >>> "+next(namesIterator))  # names[1]
print("using iterator >>> "+next(namesIterator))  # names[2]
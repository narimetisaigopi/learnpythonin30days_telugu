age = 23

my_first_message = "Hello Dev"

'''
* starts with A-Z.a-z,_ 
* not starts numberwith 0-9
* case senstive 
* Case Senstive
'''

name = "Sai Gopi"
Name = "Divya"
namE = "Ashok"


# print(name)
# print(Name)
# print(namE)

#lengthy
x = 10
y = 23
z = 34

x,y,z = 10,23,34

print(y)

x = y = z = 123

print(x)
print(y)
print(z)

age = "25"

print("My Age is " + age)


temp = "My name is "
name = "Sai Gopi"

print(temp + name)

#### global

print("#####################")

name = "Sai Gopi" # global scope

def doSomeThing():
    global name # it is converting local variable to global variable
    name = "Tech Telugu"  # local scope


doSomeThing()
print(name)


'''
Quiz
1) N_ame
2) 99Sale_Today
'''




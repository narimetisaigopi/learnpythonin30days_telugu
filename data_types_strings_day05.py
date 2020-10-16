print("Hello Sai Gopi")

#single line 
name = "Sai Gopi 798"
name2 = 'Sai Gopi 798'
print(name2)

#multi line strings
about_me = ''' i am sai gopi,
i am teaching python to telugu people
i am from khammam
'''

print(about_me)

# arry
x = "Hello World" #=>> ['H','e','l','l','o']
x = "Hello World" #=>> [0,  1,  2,   3 , 4 ] indexing
print(x[1])

#slicing
print(x[0:5])

#len
print(len(about_me))

x = "   Hello World  "
print(x)
print(x.strip())

print(x.lower())
print(x.upper())

x = "hello,iam,sai"
print(x.replace('sai','Gopi'))

print(x.split(","))

x = "hello "
y = "world"

# concatenation
print(x+y)

age = 24
temp = "{}: my age is {}"
print(temp.format("Sai",age))

x = "my world by mr. \"gopi\""

print(x)


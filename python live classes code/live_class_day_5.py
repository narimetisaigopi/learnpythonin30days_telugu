# function or method


#creator function
#aruguments
def my_function(name,name2):
    print("Hello world from = ")

#calling function
# parameters
my_function("Sai Gopi","Narimeti")

def my_function2(*name):
    print("Hello world from F2 "+name[1])

my_function2("bharath","sas")


def add_numbers(x,y):
    #z = x + y
    return x+ y

result = add_numbers(12,8)
print("result "+str(result))


def print_my_country(age = 18,country = "India"):
    print("My country is "+country+" and age is "+str(age))

print_my_country(country="usa",age=24)
print_my_country(36)

#pass
# empty function
def i_do_nothing():
    pass

i_do_nothing()




    







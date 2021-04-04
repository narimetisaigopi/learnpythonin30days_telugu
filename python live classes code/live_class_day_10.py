# Exception Handing
# try 
# expect 
# finally 
# rise

# compile time errors and runtime error => exception

#int aa = "22"
try:
    y = 0
    x = 80 / 0 #ZeroDivisionError
    print(y)
except ZeroDivisionError:
    print("ZeroDivisionError exception has occured.")
except NameError:
    print("given not found exception has occured.")
except:
    print("Something went wrong")
else: # only executes no error occurred
    print("all went in the code")
finally: # only executes either no error or error occurred
    print("all the time i will be execute")

age = 17

#17/0 # ZeroDivisionError: division by zero

if age < 18: #Exception: You are not eligible for voting
    raise Exception("You are not eligible for voting") 




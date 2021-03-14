# classes and objects

# 1) properties (variables)
# 2) methods (functions)

#class = properities + methods

#Human
# color = white,height =5.6inche,gender,....
# work(), study(), walking(), sleeping()
# https://google.github.io/styleguide/pyguide.html

# def myClass():
class MyClass:
    
    def __init__(self,height,work):
        self.height = height
        self.work = work
        print("MyClass obj has created")

    
    def iDoWork(self,name):
        print(name+" do "+self.work)

class IWillDoNothing:
    pass



myClassObj = MyClass(23,"Teaching...")

myClassObj.height = 29
print(myClassObj.height)
print(myClassObj.iDoWork("Sanju"))

myClassObjSai = MyClass(25,"Software")
print(myClassObjSai.height)
print(myClassObjSai.iDoWork("Sai"))







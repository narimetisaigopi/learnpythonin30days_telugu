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
    # Global Scope
    # Local Scope

    name = "Audi"
    
    def __init__(self,height,work):
        
        self.height = height # global scope
        self.work = work
        #print(str(self.height)+" do "+self.work)
        #print("MyClass obj has created")

    
    def iDoWork(self,sas):
        # View
        # view
        name = "Ferrai"
        print(str(self.height)+" do "+self.work)
        print("i have nothing")

    def printBrandName(self):
        self.name = "Ferrai"
        print("Brand name is "+self.name)

    def printBrandName2(self):
        print("Brand name 2 is "+self.name)



    def getNumberOfWheels(self,wheels = 4):
        return "This "+self.name+" has "+str(wheels)+" wheels"

class IWillDoNothing:
    pass



myClassObj1 = MyClass(23,"Teaching...")
myClassObj1.printBrandName2()
myClassObj1.printBrandName()



# myClassObj2 = MyClass(25,"Software")
# print(myClassObj2.height)
# print(myClassObj2.iDoWork("Sai"))







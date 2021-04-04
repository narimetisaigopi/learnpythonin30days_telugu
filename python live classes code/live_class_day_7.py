# inheritance


#parent class
class Person:
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
        print("Person obj created")

    def displayName(self):
        print("Name is "+self.name)

    def displayRollNo(self):
        print("Roll Number  is "+str(self.rollNo))

# per = Person("Sai Gopi",890)

# per.displayName()
# per.displayRollNo()

#child class
class Student(Person):
    def __init__(self, name, rollNo):
        super().__init__(name, rollNo)
        print("Student obj created")

    super().name = "sai gopi"
    __self__.name = "Gopal"

    #overwriting
    def displayName(self,name):
        print("i am child "+name)

stud = Student("Vicky",345)

stud.displayName("sai")
stud.displayRollNo()

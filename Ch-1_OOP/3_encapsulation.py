class MyClass:

    # Class variables
    var1 = "Ansh"
    var2 = "Lamba"

    # Instance Variables
    def __init__(self,dyn1,dyn2,dyn3):
        self.dyn1 = dyn1 #Public Variable
        self.__dyn2 = dyn2 #Private Variable
        self._dyn3 = dyn3 #Protected Variable

    def func1(self):
        print(f"Hello World, {self.dyn1}")

    def func2(self):
        print(f"Hello Globe, {self.__dyn2}")

    def func3(self):
        print(f"Hello Globe, {self._dyn3}")


obj = MyClass("abc","def","xyz")
obj.dyn1 = "pqr"
print(obj.dyn1)
obj.func1() # It will print "Hello World, pqr" because we have changed the value of dyn1 to "pqr" and it is a public variable.

# This will not give error but it will create a new variable dyn2 in the object and assign the value "stu" to it. It will not change the value of __dyn2 which is a private variable.
obj.dyn2 = "stu"
print(obj.dyn2) 
obj.func2() # It will print "Hello Globe, def" because the value of __dyn2 is still "def" and it is not changed by obj.dyn2 = "stu" statement.


print(obj._dyn3) # It will print "xyz" because _dyn3 is a protected variable and it can be accessed outside the class but it is not recommended to do so. It is just a convention to use _ before the variable name to indicate that it is a protected variable and it should not be accessed outside the class.
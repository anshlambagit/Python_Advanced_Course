class MyClass:

    my_var = 100

    # Dunder method or magic method
    def __init__(self):
        print("This is the constructor method")

    # Dunder method for str 
    def __str__(self):
        return "This is the string representation of the object"

    @classmethod
    def _change_value(cls,new_value):
        cls.my_var = new_value

    @staticmethod
    def dummy():
        print("This is a dummy method")

# obj = MyClass()
# print(obj.my_var) # 100
# obj._change_value(200)
# print(obj.my_var) # 200
# obj2 = MyClass()
# print(obj2.my_var) # 200
# obj3 = MyClass()
# print(obj3.dummy())
obj4 = MyClass()
print(obj4)
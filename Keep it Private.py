class my_class:
    __privar=27
    def __privMeth(self):
        print("I am Inside the class my class")
    def hello(self):
        print ("the value of the variable is:",my_class.__privar)
hey=my_class()
hey.hello()
hey.__privMeth
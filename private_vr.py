class myClass:
    __privateVar = 27;
    def __privMeth(self):
        print("I am inside class myClass")
    def hello(self):
      print("Private Variable value", myClass.__privateVar)


x = myClass()
x.hello()
x.__privMeth()

class Parent:
    def function1(self):
        print("This is function one")

class child(Parent):
            def function2(self,a):
                print("This is function two")
                print(a)
            b=10

y=child()
y.function1()
y.function2(10)
print(y.b)
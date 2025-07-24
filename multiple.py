class Parent:
    def show1(self):
        print("Hi this is parent")
class child1(Parent):
    def show2(self):
        print("Hi this is first child")
class child2(Parent):
    def show3(self):
        print("Hi this is second Child ")
obj=child1()
obj.show2()
obj.show1()
obj=child2()
obj.show3()

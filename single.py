class Parent:
    def show1(self):
        print("this is parent1 class")
    def show2(self):
        print("this is parent2 class")
class Child(Parent):
    def show3(self):
        print("This is child class")
obj = Child()
obj.show3()
obj.show2()
obj.show1()
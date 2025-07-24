class Parent:
    def show1(self):
        print("this is parent1 class")
    def show2(self):
        print("this is parent2 class")
class Child(Parent):
    def show3(self):
        print("This is child class")
class GrandChild(Child):
    def show4(self):
        print("Hi this is  grandchild")
obj = GrandChild()
obj.show4()
obj.show3()
obj.show2()
obj.show1()
class Father:
    def show1(self):
        print("Hi this is father")
class Mother:
    def show2(self):
        print("Hi this is mother")
class child(Mother,Father):
    def show3(self):
        print("Hi this is Child class")
obj=child()
obj.show3()
obj.show2()
obj.show1()
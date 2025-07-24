#Overloading
# same class 
# same functions or Methods
# different parameters
class Car:
    def show(self,a,b):
        return a+b
class Car:
    def show(self,a,b,c=0):
        return a+b+c
obj= Car()
print(obj.show(2,434))
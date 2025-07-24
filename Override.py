#Overriding
# different class 
# same functions or Methods
# different parameters
class Car:
    def show(self, a, b):
        return a + b

class Jeep(Car):  # ✅ Inheriting from Car
    def show(self, a, b, c=0):
        print("Jeep version called")
        return a + b + c

obj = Jeep()
print(obj.show(2, 434))        # Output: 436
print(obj.show(2, 434, 10))    # Output: 446

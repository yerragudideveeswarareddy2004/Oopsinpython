class Car:
    def __init__(self):
        print("Hi this is my super car")
        
    def drive(self, model, brand):
        self.model = model
        self.brand = brand
        print(self.model, self.brand)

# Object creation (no args to __init__)
obj = Car()

# Calling drive with arguments
obj.drive('3', '4')

class Vehicle:
    def __init__(self,a,b,c):
        self.__a=a
        self._b=b
        self.c=c
    def start(self):
        print(self.__a)
        print(self._b)
        print(self.c)
obj=Vehicle(3,4,7)
obj.start()


print(obj.c)
print(obj._b)
print(obj.__a)

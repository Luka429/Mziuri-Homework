class Rentangle:
    def __init__(self,length,width):
        self.width = width
        self.length = length

    def perimeter_finder(self):
        return ((self.width + self.length) * 2)
    def area_finder(self):
        return(self.width * self.length)

obj1 = Rentangle(5,10)
print(obj1.area_finder())
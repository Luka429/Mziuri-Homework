#სავარჯიშო 1
from locale import currency


class Cat:
    def eat(self):
        return "Cat eats a milk"

    def talk(self):
        return "cat says miaww"

    def walk(self):
        return "Cat can run 20km/h"

class Dog:
    def eat(self):
        return "dog eats a bone"

    def talk(self):
        return "dog says aww"

    def walk(self):
        return "Dog can run 40km/h"

dog1 = Dog()
cat1 = Cat()

print(dog1.talk(),dog1.walk(),dog1.eat())
print(cat1.talk(),cat1.walk(),cat1.eat())

#სავარჯიშო 2

class Currency:
    def __init__(self,value,unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f'{self.unit}.{self.value}'

    def changeto(self,newunit):
        if self.unit =="GEL" and newunit == "USD":
            return f'{newunit}.{self.value / 2.7}'

        elif self.unit == "GEL" and newunit == "EUR":
            return f'{newunit}.{self.value / 3}'

        elif self.unit == "USD" and newunit == "GEL":
            return f'{newunit}.{self.value * 2.7}'

        elif self.unit == "USD" and newunit == "EUR":
            return f'{newunit}.{self.value * 1.11}'

        elif self.unit == "EUR" and newunit == "GEl":
            return f'{newunit}.{self.value * 3}'

        elif self.unit == "EUR" and newunit == "USD":
            return f'{newunit}.{self.value * 1.11}'

        elif self.unit == newunit:
            return f'{self.unit}.{self.value}'

        else:
            return "Please Enter real units"

    def addition (self, other):
        if self.unit == other.unit:
            return Currency(self.value + other.value, self.unit)
        else:
            converted_unit = other.changeto(self.unit)
            return Currency(self.value + converted_unit.value, self.unit)


    def multiplication(self,num):

        if num != int or num != float:
            raise TypeError("“გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე")

        return currency(self.value * num,self.unit)



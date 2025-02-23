class Person:
    def __init__(self, name, deposit = 1000, loan = 0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"name: {self.name},deposit amount: {self.deposit}, loan amount: {self.loan}"

class House:
    def __init__(self,ID,price,owner,status = "For sale"):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status


    def Sell_House(self,person,loan = None):
        if loan is None and self.status == "For sale":
            person.deposit += self.price
            self.owner = person.name
            self.status = "Sold"
            return f"Congrats you have just bought the house,you {person.name} are the new owner"

        elif self.status =="Sold" or self.status == "Sold by loan":
            return "This house been sold and is no longer available"

        elif self.status == "For sale":
            self.owner.deposit = self.owner.deposit + self.price
            self.owner = person
            self.status = "Sold by loan"
            person.loan += self.price
            return f"Congrats you have just bought the house by loan,you {person.name} are the new owner"

person1 = Person('genadi japaridze')
person2 = Person('gela barkalaia')
house1 = House(1612,50000,person1,'For sale')
print(house1.Sell_House(person2))
print(person1.__str__())









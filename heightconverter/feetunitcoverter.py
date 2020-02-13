class Feet:

    def __init__(self, quantity):
        self.quantity = quantity
      
    def toinch(self):
        return self.quantity*12

    def tokilometer(self):
        return round(self.quantity/3281, 7)

    def tometer(self):
        return round(self.quantity/3.281, 4)

    def tocntimeter(self):
        return self.quantity*30.48

    def tomillimetre(self):
        return self.quantity*304.8

    def tomicrometre(self):
        return self.quantity*304800

    def tomile(self):
        return round(self.quantity/5280, 9)

    def toyard(self):
        return round(self.quantity/3, 6)

    def tonauticalmile(self):
        return round(self.quantity/6076, 9)


myobject = Feet(1)
# print(myobject.toinch())
# print(myobject.tokilometer())
# print(myobject.tometer())
# print(myobject.tocntimeter())
# print(myobject.tomillimeter())
print(myobject.tonauticalmile())

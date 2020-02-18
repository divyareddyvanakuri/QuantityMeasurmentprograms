from lengths import Inchunit,FeetUnit,CentiMeterUnit,Length

class Qunatity:
    def __init__(self,value,unit):
        self.value = value
        self.unit = unit
    def __add__(self,other):
        self.factor = int(self.unit.comparison_to_base(self.value))
        other.factor = int(other.unit.comparison_to_base(other.value))
        return self.factor+other.factor


#2inch+2inch
first_inch_objcet=Qunatity(2,Inchunit())
second_inch_object=Qunatity(2,Inchunit())
z=first_inch_objcet+second_inch_object
print("add two lengths 2inch and 2inch in inches:",z)

#1ft+2inch
one_feet_object=Qunatity(1,FeetUnit())
two_inch_objcet=Qunatity(2,Inchunit())
z=one_feet_object+two_inch_objcet
print("add two lengths  1ft and 2inch in inches:",z)

#1ft+1ft
first_feet_object=Qunatity(1,FeetUnit())
second_feet_object=Qunatity(1,FeetUnit())
z=first_feet_object+second_feet_object
print("add two lengths  1ft and 1ft in inches:",z)

#2inch+2.5cm
two_inch_objcet=Qunatity(2,Inchunit())
first_inch_object=Qunatity(2.5,CentiMeterUnit())
z=two_inch_objcet+first_inch_object
print("add two lengths  2inch and 2.5cm in inches:",z)
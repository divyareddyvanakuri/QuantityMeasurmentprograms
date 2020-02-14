from feetclass import FeetUnit
from inchclass import InchUnit

#1ft = 1ft
first_foot_object = FeetUnit(1)
second_foot_object = FeetUnit(1)
print("Is 1ft = 1ft:",first_foot_object ==second_foot_object)

#1ft = 2ft
one_feet_object = FeetUnit(1)
two_feet_object = FeetUnit(2)
print("Is 1ft = 2ft:",one_feet_object == two_feet_object)

#1inch = 1inch
first_inch_object=InchUnit(1)
second_inch_object=InchUnit(1)
print("Is 1inch = 1inch:",first_inch_object == second_inch_object)

#1inch = 2inch
one_inch_object = InchUnit(1)
two_inch_object = InchUnit(2)
print("Is 1inch = 2inch:",one_feet_object == two_feet_object)

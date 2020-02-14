from feetclass import FeetUnit
from inchclass import InchUnit
from yardclass import YardUnit

#1ft = 1ft
first_foot_object = FeetUnit(1)
second_foot_object = FeetUnit(1)
print("Is 1ft = 1ft:",first_foot_object ==second_foot_object)

#1ft != 2ft
one_feet_object = FeetUnit(1)
two_feet_object = FeetUnit(2)
print("Is 1ft = 2ft:",one_feet_object == two_feet_object)

#1inch = 1inch
first_inch_object=InchUnit(1)
second_inch_object=InchUnit(1)
print("Is 1inch = 1inch:",first_inch_object == second_inch_object)

#1inch != 2inch
one_inch_object = InchUnit(1)
two_inch_object = InchUnit(2)
print("Is 1inch = 2inch:",one_inch_object == two_inch_object)

#1yard = 1yard
first_yard_object=InchUnit(1)
second_yard_object=InchUnit(1)
print("Is 1yard = 1yard:",first_yard_object == second_yard_object)

#1yard != 2yard
one_yard_object = YardUnit(1)
two_yard_object = YardUnit(2)
print("Is 1yard = 2yard:",one_yard_object == two_yard_object)
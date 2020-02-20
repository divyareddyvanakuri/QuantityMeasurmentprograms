from ftandinchobjcls import InchUnit
from ftandinchobjcls import FeetUnit
from ftandinchobjcls import Length

#This is the composition class for feet and inch objects
class Quantity:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __eq__(self, other):
        self.factor = int(self.unit.comparisons_to_base(self.value))
        other.factor = int(other.unit.comparisons_to_base(other.value))
        if self.factor == other.factor:
            return True
        return False

# 1 inch = 1 inch
try:
    first_inch_object = Quantity("", InchUnit())
    second_inch_object = Quantity(1, InchUnit())
    print("Is 1inch = 1inch:", first_inch_object == second_inch_object)
except NameError as e:
    print("Runtime Error:",e)
except ValueError as e:
    print("Runtime Error:",e)

# 1 inch != 2 inch
three_inch_object = Quantity(1, InchUnit())
four_inch_object = Quantity(2, InchUnit())
print("Is 1inch = 2inch:", three_inch_object == four_inch_object)

# 1 ft = 1 ft
first_feet_object = Quantity(1, FeetUnit())
second_feet_object = Quantity(1, FeetUnit())
print("Is 1ft = 1ft:", first_feet_object == second_feet_object)

# 1 ft = 2 ft
three_feet_object = Quantity(1, FeetUnit())
four_feet_object = Quantity(2, FeetUnit())
print("Is 1ft = 2ft:", three_feet_object == four_feet_object)

#1 ft = 1 inch
one_feet = Quantity(1, FeetUnit())
one_inch = Quantity(1, InchUnit())
print("Is 1ft = 1 inch:",one_feet==one_inch)

# 1 ft = 12 inch
one_feet = Quantity(1, FeetUnit())
twelve_inches = Quantity(12, InchUnit())
print("Is 1ft = 12inch:", one_feet == twelve_inches)


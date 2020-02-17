from ftandyardobjcls import YardUnit
from ftandyardobjcls import FeetUnit
from ftandyardobjcls import Length

# implemented the composition class for Length
class Quantity:
    def __init__(self, value, unit):

        self.value = value
        self.unit = unit

    def __eq__(self, other):
        self.factor = str(self.unit.comparisons_to_base(self.value))
        other.factor = str(other.unit.comparisons_to_base(other.value))
        if self.factor == other.factor:
            return True
        return False


# one yard = one yard
first_one_yard = Quantity(1, YardUnit())
second_one_yard = Quantity(1, YardUnit())
print("Is 1 yard = 1 yard:", first_one_yard == second_one_yard)

# one yard != two yards
one_yard = Quantity(1, YardUnit())
two_yards = Quantity(2, YardUnit())
print("Is 1 yard = 2 yards:", one_yard == two_yards)

# one feet = one feet
first_one_feet = Quantity(1, FeetUnit())
second_one_feet = Quantity(1, FeetUnit())
print("Is 1 ft = 1 ft:", first_one_feet == second_one_feet)

# one feet != two feet
one_feet = Quantity(1, FeetUnit())
two_feet = Quantity(2, FeetUnit())
print("Is 1 ft = 2 ft:", one_feet == two_feet)

#one yard != one inch
one_yard = Quantity(1, YardUnit())
one_inch = Quantity(1, FeetUnit())
print("Is 1yard = 1ft:",one_inch == one_yard)

# one yard = three feet
one_yard = Quantity(1, YardUnit())
three_feet = Quantity(3, FeetUnit())
print("Is 1 yard = 3 ft:", one_yard == three_feet)


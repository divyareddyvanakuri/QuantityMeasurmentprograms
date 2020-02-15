from abc import ABC, abstractmethod


class Length(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    @abstractmethod
    def __comparisons_to_base(self, value):
        return value * self.conversion_factor


class InchUnit(Length):
    def __init__(self):
        super().__init__(1)


class FeetUnit(Length):
    def __init__(self):
        super().__init__(12)


class Quantity(Length):
    def __init__(self, value, unit):
        self.value = value
        print(self.value)
        self.unit = unit
        super(Length, self).__init__()
        print(self._Length__comparisons_to_base(self.value))

    def _Length__comparisons_to_base(self,value):
        pass

    def __eq__(self, other):
        if self.value  == other.value:
            return True
        return False
    


# 1 inch = 1 inch
first_inch_object = Quantity(1, InchUnit)
second_inch_object = Quantity(1, InchUnit)
print("Is 1inch = 1inch: ", first_inch_object == second_inch_object)
# 1 inch != 2 inch
three_inch_object = Quantity(1, InchUnit)
four_inch_object = Quantity(2, InchUnit)
print("Is 1inch = 2inch: ", three_inch_object == four_inch_object)

# 1 ft = 1 ft
first_feet_object = Quantity(1, FeetUnit)
second_feet_object = Quantity(1, FeetUnit)
print("Is 1ft = 1ft: ", first_feet_object == second_feet_object)

# 1 ft = 2 ft
three_feet_object = Quantity(1, FeetUnit)
four_feet_object = Quantity(2, FeetUnit)
print("Is 1ft = 2ft: ", three_feet_object == four_feet_object)

one_feet = Quantity(1, FeetUnit)
twelve_inches = Quantity(12, InchUnit)

print("Is 1ft = 12inches: ", one_feet == twelve_inches)

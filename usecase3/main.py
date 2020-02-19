from lenght import Length, InchUnit, CentiMeterUnit

#Implemented the composition class for length
class Qunatity:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __eq__(self, other):
        self.factor = str(self.unit.comparison_to_base(self.value))
        other.factor = str(other.unit.comparison_to_base(other.value))
        if self.factor == other.factor:
            return True
        return False


# 1 inch = 1 inch
first_inch_object = Qunatity(1, InchUnit())
second_inch_object = Qunatity(1, InchUnit())
print("Is 1 inch = 1 inch:", first_inch_object == second_inch_object)

# 1 inch != 2 inch
one_inch_object = Qunatity(1, InchUnit())
two_inch_object = Qunatity(2, InchUnit())
print("Is 1 inch = 2 inch:", one_inch_object == two_inch_object)

# 1 cm = 1 cm
first_cm_object = Qunatity(1, CentiMeterUnit())
second_cm_object = Qunatity(1, CentiMeterUnit())
print("Is 1 cm = 1 cm:", first_cm_object == second_cm_object)

# 1 cm != 2 cm
one_cm_object = Qunatity(1, CentiMeterUnit())
two_cm_object = Qunatity(2, CentiMeterUnit())
print("Is 1 cm = 2 cm:", one_cm_object == two_cm_object)

# 1 cm != 1 inch
one_cm_object = Qunatity(1, CentiMeterUnit())
one_inch_object = Qunatity(1, InchUnit())
print("Is 1 cm = 1 inch:", one_cm_object == one_inch_object)

# 2 inch = 5 cm
two_inch_object = Qunatity(2, InchUnit())
five_cm_object = Qunatity(5, CentiMeterUnit())
print("Is 2 inch = 5 cm:", two_inch_object == five_cm_object)

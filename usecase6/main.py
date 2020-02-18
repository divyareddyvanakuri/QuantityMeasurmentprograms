from volumes import Volumes, LitreUnit, GallonUnit, MlUnit


class Qunatity:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __add__(self, other):
        self.factor = float(self.unit.comparison_to_base(self.value))
        other.factor = float(other.unit.comparison_to_base(other.value))
        return self.factor+other.factor


# 1 gallon + 3.78 litres
one_gallon_object = Qunatity(1, GallonUnit())
litre_object = Qunatity(3.78, LitreUnit())
z = one_gallon_object+litre_object
print("add two volumes 1 gallon and 3.78 litres in litres:", z)

# 1 litre + 1000 ml
one_litre_object = Qunatity(1, LitreUnit())
one_ml_obeject = Qunatity(1000, MlUnit())
z = one_litre_object+one_ml_obeject
print("add two volumes 1 litre and 1000 ml in litres:", z)

from volume import Volume,GallonUnit,LitreUnit,MlUnit

#Implemented the Composition class for volume
class Qunatity:
    def __init__(self,value,unit):
        self.value = value
        self.unit = unit

    def __eq__(self,other):
        self.factor = float(self.unit.comparison_to_base(self.value))
        other.factor = float(other.unit.comparison_to_base(other.value))
        if self.factor == other.factor:
            return True
        return False


#1 gallon = 1 gallon
first_gallon_object = Qunatity(1,GallonUnit())
second_gallon_object = Qunatity(1,GallonUnit())
print("Is 1 gallon = 1 gallon:",first_gallon_object == second_gallon_object)

#1 gallon != 2 gallon
one_gallon_object = Qunatity(1,GallonUnit())
two_gallon_object = Qunatity(2,GallonUnit())
print("Is 1 gallon = 2 gallon:",one_gallon_object == two_gallon_object)

#1 litre = 1 litre
first_litre_object = Qunatity(1,LitreUnit())
second_litre_object = Qunatity(2,LitreUnit())
print("Is 1 litre = 1 litre:", first_litre_object == second_litre_object)

# 1 litre != 2 litres
one_litre_object = Qunatity(1,LitreUnit())
two_litres_object = Qunatity(2,LitreUnit())
print("Is 1 litre = 2 litres:",one_litre_object == two_litres_object)

# 1 gallon = 1 litre
one_gallon_object = Qunatity(1,GallonUnit())
one_litre_object = Qunatity(1,LitreUnit())
print("Is 1 gallon = 1 litre:", one_gallon_object == one_litre_object)

# 1 gallon = 3.78 litres
one_gallon_object = Qunatity(1,GallonUnit())
litres_object = Qunatity(3.78,LitreUnit())
print("Is 1 gallon = 3.78 litres:",one_gallon_object == litres_object)

#1 litre != 1ml
one_litre_object = Qunatity(1,LitreUnit())
one_ml_object = Qunatity(1,MlUnit())
print("Is 1 litre = 1 ml:",one_litre_object == one_ml_object)

# 1 litre = 1000 ml
litre_object = Qunatity(1,LitreUnit())
ml_object = Qunatity(1000,MlUnit())
print("Is 1 litre = 1000 ml:",litre_object == ml_object)
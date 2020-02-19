from weights import KgUnit, GramUnit, TonneUnit

#Implemented the composition class for weight
class Qunatity:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
    
    def __eq__(self, other):
        self.factor = int(self.unit.comparison_to_base(self.value))
        other.factor = int(other.unit.comparison_to_base(other.value))
        if self.factor == other.factor:
            return True
        return False

    def __add__(self, other):
        self.factor = int(self.unit.comparison_to_base(self.value))
        other.factor = int(other.unit.comparison_to_base(other.value))
        return self.factor+other.factor


# 1 kg = 1000 grams
one_kg_object = Qunatity(1, KgUnit())
grams_object = Qunatity(1000, GramUnit())
print("Is 1 kg = 1000 grams:", one_kg_object == grams_object)

# 1 tonne = 1000 kg
tonne_object = Qunatity(1, TonneUnit())
kg_object = Qunatity(1000, KgUnit())
print("Is 1 tonne = 1000 kg:", tonne_object == kg_object)

# 1 tonne + 1000 grams
tonne_object = Qunatity(1, TonneUnit())
grams_object = Qunatity(1000, GramUnit())
z = tonne_object+grams_object
print("Add two weights 1 tonne and 1000 grams in kg:", z)

from abc import ABC, abstractmethod


#Abstract class for weight
class Weights(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    def comparison_to_base(self, value):
        return value*self.conversion_factor


#Derived class from the base class
class KgUnit(Weights):
    def __init__(self):
        super().__init__(1)


#Derived class from the base class
class GramUnit(Weights):
    def __init__(self):
        super().__init__(1/1000)


#Derived class from the base class
class TonneUnit(Weights):
    def __init__(self):
        super().__init__(1000)

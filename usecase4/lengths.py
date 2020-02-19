from abc import ABC, abstractmethod


# Abstract class for Length
class Length(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    def comparison_to_base(self, value):
        return value*self.conversion_factor


# Derived class from the base class
class Inchunit(Length):
    def __init__(self):
        super().__init__(1)


# Derived class from the base class
class FeetUnit(Length):
    def __init__(self):
        super().__init__(12)


# Derived class from the base class
class CentiMeterUnit(Length):
    def __init__(self):
        super().__init__(2/5)

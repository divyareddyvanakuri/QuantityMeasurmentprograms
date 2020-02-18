from abc import ABC, abstractmethod


class Length(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    
    def comparison_to_base(self, value):
        return value*self.conversion_factor


class InchUnit(Length):
    def __init__(self):
        super().__init__(5)


class CentiMeterUnit(Length):
    def __init__(self):
        super().__init__(2)

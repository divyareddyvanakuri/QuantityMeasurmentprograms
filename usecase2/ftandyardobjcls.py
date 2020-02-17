from abc import ABC, abstractmethod

#Abstract class
class Length(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    def comparisons_to_base(self, value):
        return value*self.conversion_factor

#child class
class YardUnit(Length):
    def __init__(self):
        super().__init__(3)

#child class
class FeetUnit(Length):
    def __init__(self):
        super().__init__(1)


 
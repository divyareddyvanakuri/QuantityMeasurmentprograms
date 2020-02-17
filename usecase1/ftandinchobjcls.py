#This is the inheritance class to convert units from inch to feet and viseversa

from abc import ABC, abstractmethod


class Length(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    
    def comparisons_to_base(self,value):
        return value*self.conversion_factor


class InchUnit(Length):
    def __init__(self):
        super().__init__(1)


class FeetUnit(Length):
    def __init__(self):
        super().__init__(12)



        
    




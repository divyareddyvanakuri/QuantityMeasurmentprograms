from abc import ABC, abstractmethod


class Height(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    
    def comparisons_to_base(self,value):
        return value*self.conversion_factor


class InchUnit(Height):
    def __init__(self):
        super().__init__(1)


class FeetUnit(Height):
    def __init__(self):
        super().__init__(12)



        
    




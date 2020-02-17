from abc import ABC, abstractmethod


class Length(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    @abstractmethod
    def comparisons_to_base(self):
        pass


class InchUnit(Length):
    def __init__(self):
        super().__init__(1)


class FeetUnit(Length):
    def __init__(self):
        super().__init__(12)



        
    




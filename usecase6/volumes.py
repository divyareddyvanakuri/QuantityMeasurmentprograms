from abc import ABC, abstractmethod



# Abstract class for Volume
class Volumes(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    def comparison_to_base(self, value):
        return value*self.conversion_factor



#Derived class from the base class
class LitreUnit(Volumes):
    def __init__(self):
        super().__init__(1)

#Derived class from the base class
class GallonUnit(Volumes):
    def __init__(self):
        super().__init__(3.78)

#Derived class from the base class
class MlUnit(Volumes):
    def __init__(self):
        super().__init__(1/1000)

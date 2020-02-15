from abc import ABC, abstractmethod


class Height(ABC):
    def __init__(self, value,conversion_factor):
        self.value = value
        self.conversion_factor = conversion_factor

    
    @abstractmethod
    def comparisons_to_base(self):
        pass

class FeetUnit(Height):
    def __init__(self):
        super().__init__(0.3048)

class InchUnit(Height):
    def __init__(self):
        super().__init__(0.0254)
   

class YardUnit(Height):
    def __init__(self):
        super().__init__(0.9144)

class meterUnit(Height):
    def __init__(self):
        super().__init__(1)


class Quantity(Height):
    def __init__(self, value, conversion_factor):
        # super().__init__(value, conversion_factor)
        self.comparisons_to_base()

    def __eq__(self, other):
        print(self.conversion_factor)
        print(other.conversion_factor)
        print(other.value)
        print(self.value)
    
        if other.value<self.value:
            other.value=other.value*12
        elif other.value>self.value:
             other.value=int(other.value/12)
        else:
            return False
        print(other.value)
        print(self.value)
        if self.value == other.value:
            if isinstance(other,self.__class__):
                return True
        return False
        print(self.conversion_factor)
        print(other.conversion_factor)
    def comparisons_to_base(self):
        pass

one_Feet = Quantity(1,FeetUnit)
twelve_inch = Quantity(12,InchUnit)
print(one_Feet == twelve_inch)
one_Feet = Quantity(1,FeetUnit)
twelve_inch = Quantity(1,InchUnit)
print(one_Feet == twelve_inch)

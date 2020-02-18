from abc import ABC, abstractmethod


class Weights(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    def comparison_to_base(self, value):
        return value*self.conversion_factor


class KgUnit(Weights):
    def __init__(self):
        super().__init__(1)


class GramUnit(Weights):
    def __init__(self):
        super().__init__(1/1000)


class TonneUnit(Weights):
    def __init__(self):
        super().__init__(1000)

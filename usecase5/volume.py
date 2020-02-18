from abc import ABC, abstractmethod


class Volume(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    def comparison_to_base(self, value):
        return value*self.conversion_factor


class GallonUnit(Volume):
    def __init__(self):
        super().__init__(3.78)


class LitreUnit(Volume):
    def __init__(self):
        super().__init__(1)


class MlUnit(Volume):
    def __init__(self):
        super().__init__(1/1000)

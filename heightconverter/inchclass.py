class InchUnit:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, InchUnit):
            if other.value == self.value:
                return True
        return False

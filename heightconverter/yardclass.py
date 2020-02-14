class YardUnit:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, YardUnit):
            if other.value == self.value:
                return True

        return False


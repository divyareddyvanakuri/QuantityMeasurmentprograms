class Height:
    def __init__(self, value):
        self.value


class FeetUnit(Height):
    def __init__(self):
        super.__init__(1)


class InchUnit(Height):
    def __init__(self):
        super.__init__(12)


class YardUnit(Height):
    def __init__(self):
        super.__init__(0.333333)


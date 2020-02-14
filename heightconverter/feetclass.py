class Feet:
    def __init__(self,value):
        self.value=value
    def __eq__(self,other):
        if  isinstance(other,Feet):
            return True
        else:
            return False
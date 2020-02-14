class Height:
    def __init__(self,x,y,z):
        self.ft=x
        self.inch=y
        self.yard=z
    def __eq__(self,other):
        if other.ft == self.ft and other.inch == self.inch and other.yard == self.yard:
            return "both objects are equal"
        else:
            return "both objects are not equal"
h1=Height(2,3,4)
h2=Height(5,6,7)
print(h1 == h2)
h3=Height(2,3,4)
h4=Height(2,3,4)
print(h3 == h4)
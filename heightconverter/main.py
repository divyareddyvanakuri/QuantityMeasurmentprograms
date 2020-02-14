from feetclass import Feet
from inchclass import inch
first_one_feet=Feet(1)
second_on_feet=Feet(2)
try:
    assert first_one_feet == second_on_feet
    print("successful")
except AssertionError as e:
    print(e)





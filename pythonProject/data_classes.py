# Data classes are a feature introduced in Python 3.7 to simplify the creation of
# classes primarily used to store data.

from dataclasses import dataclass


# dataclass makes the code like below
# class Person:
#     def __init__(self, name=None, age=None, mobile=None, address=None):
#         self.name = name
#         self.age = age
#         self.mobile = mobile
#         self.address = address


@dataclass
class Person:
    name: str = None
    age: int = None
    mobile: str = None
    address: str = None


person1 = Person("Hari", 34, "9010454646")
# person1.address = "abc"

# print(person1)

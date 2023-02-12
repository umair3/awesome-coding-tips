"""
No code should be forced to depen on methods it does not use.
In the below example we are segregating Driveable interface into 
multiple interaces including DrivableOnRoad, Flyable, Rideable.
"""
from abc import ABC, abstractmethod


class Driveable(ABC):
    pass


class DrivableonRoad(ABC):
    pass

class Flyable(ABC):
    pass

class Rideable(ABC):
    pass

class Steerable(ABC):
    pass
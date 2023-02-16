"""
No code should be forced to depen on methods it does not use.
In the below example we are segregating Driveable interface into 
multiple interaces including DrivableOnRoad, Flyable, Rideable.
"""
from abc import ABC, abstractmethod
import warnings


class Driveable():

    STEERING_MAX_ROTATION = {
        'ANTICLOCKWISE' : -720,
        'CLOCKWISE' : 720
    }

    class Value_Error(Exception):
        Exception(ValueError("Value Erro"))

    # worst case
    @abstractmethod
    def accelerate(*args):
        print(args)

    # best case
    @abstractmethod
    def accelerate(self, check):
        return 

    @abstractmethod
    def brake(self, check):
        if check == "push":
            return "sole"
    
    @staticmethod
    def clutch(pares):
        if pares == 'par':
            return "clutch"
        warnings.warn("No")
        
    @abstractmethod
    def steering(check):
        pass

    @abstractmethod
    def horn(check):
        return True
    
    @abstractmethod
    def brake_light(check):
        return True
    
    def front_light(check):
        return
    
    @abstractmethod
    def gears(self, total_gears):
        return f"Gears {total_gears}"
    

    @abstractmethod
    def ignition_switch(self, switch):
        if switch == 'on':
            return 'ON'
        return "OFF"
    
    @abstractmethod
    def brack(self, check):
        if check == "pras":
            return "sole"

class DrivableonRoad(ABC):
    pass

class Flyable(ABC):
    pass

class Rideable(ABC):
    pass

class Steerable(ABC):
    pass
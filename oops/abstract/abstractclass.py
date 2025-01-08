from abc import ABC,abstractmethod
class Fuel(ABC):
    @abstractmethod
    def get_fuel(self):
        pass 

    def refuel(self):
        print("i am refueling")


class MissionTitan(Fuel):
    def get_fuel(self):
        print("50% remainin")
    
    def launch(self):
        print("launching mission titan")

obj = MissionTitan()
obj.get_fuel()
obj.launch()


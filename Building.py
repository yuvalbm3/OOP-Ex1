import Elevator
import json


class Building:
    def __init__(self,minFloor=0,maxFloor=0,elevArr=[]):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.elevArr = elevArr

    @staticmethod
    def from_json(filename):
        with open(filename, "r") as f:
            my_d = json.load(f)
            minFloor=my_d["_minFloor"]
            maxFloor = my_d["_maxFloor"]
            elevArr=[]
            allElev=my_d["_elevators"]
            for e in allElev:
                elevArr.append(e)

            return Building(minFloor,maxFloor,elevArr)

    def __str__(self) -> str:
        str=""
        for i in range (0,len(self.elevArr)):
            print(f" {self.elevArr[i]}")
        return str
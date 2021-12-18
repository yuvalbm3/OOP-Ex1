import csv

from Elevator import *
from Calls import Calls
from main import main


class Algo:
    def __init__(self, building, cList, output):
        self.building = building
        self.cList = cList
        self.output = output

    def main(self, building, cList, output):
        self.building = building
        self.cList = cList
        self.output = output
        elevator_list = Elevator.elevator_list(self.building)
        outputCalls = []
        while len(self.cList) != 0:
            for i in range(len(elevator_list)):
                floor = 0
                elev = elevator_list[i]
                finishTime = 0
                for j in self.cList:
                    if (j < finishTime or j.src > elev.maxFloor or j.src < j.minFloor or
                            j.dest < elev.minFloor or j.dest > elev.maxFloor):
                        continue
                    direction = j.dirct
                    travel_time = self.totalTime(j, floor, elev)
                    floor = j.floor
                    j.assignment = i
                    outputCalls.append(j)
                    self.cList.remove(j)
                    for call in self.cList:
                        if direction == call.dirct and travel_time > call.time:
                            if direction == False and (call.dest > j.dest or call.src < floor):
                                continue
                            elif direction == True and (call.dest < j.dest or call.src > floor):
                                continue
                            else:
                                floor = call.destination
                                self.cList.remove(call)
                                call.assignment = i
                                outputCalls.append(call)
                        elif call.time >= finishTime:
                            break

        outputCalls.sort(outputCalls[1])
        Calls.writeToCsv(outputCalls, self.output)

    def callsToCsv(callsList, outputFile):
        all = []
        for i in callsList:
            all.append(i.__dict__.values())
        with open(outputFile, 'w', newline="") as file:
            csvWriter = csv.writer(file)
            csvWriter.writerows(all)

    def totalTime(call, floor, elevator):
        if floor != call.source:
            startTime = 2 * elevator.startTime
        else:
            startTime = elevator.startTime

        if floor != call.source:
            stopTime = 2 * elevator.stopTime
        else:
            stopTime = elevator.stopTime
            closeTime = 2 * elevator.closeTime
            openTime = 2 * elevator.openTime
            travelTime = (abs(floor - call.source) / elevator.speed +
                          abs(call.source - call.destination) / elevator.speed)
        return call.time + startTime + stopTime + closeTime + openTime + travelTime


if __name__ == '__main__':
    main()
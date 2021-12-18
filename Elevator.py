class Elevator:
    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime):
        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.starTime = startTime
        self.stopTime = stopTime

    def to_list(self):
        return ['Elevator call', self.time, self.source,
                self.destination, 0, self.assignment]


def elevator_list( Building):
    elevator_list = []
    sb = Building[2]
    for i in len(sb):
        elevator_list.append(Building[2][i])
    return elevator_list
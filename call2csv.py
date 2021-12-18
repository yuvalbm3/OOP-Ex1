import csv


class call2csv:
    def __init__(self, name="", callTime=0, src=0, dest=0, statues=0, index=0):
        self.name = name
        self.callTime = callTime
        self.src = src
        self.dest = dest
        self.statues = statues
        self.index = index

    def callsList(self, cList):
        self.time = float(cList[1])
        self.src = int(cList[2])
        self.dest = int(cList[3])
        if self.src > self.dest:
            self.direction = False
        elif self.src < self.dest:
            self.direction = True
        self.assignment = cList[5]

    def __repr__(self):
        return f'time: {self.callTime} src: {self.src} ' \
               f'dst: {self.dst} status:{self.statues} best elevator:{self.index}'

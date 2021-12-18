import csv


class Calls:
    def __init__(self, name, callTime, src, dest, statues, index):
        self.name = name
        self.callTime = callTime
        self.src = src
        self.dest = dest
        self.statues = statues
        self.index = index

    @staticmethod
    def loadFromCSV(file):
        callsList = []
        with open(file) as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                call = Calls(line[1], line[2], line[3], line[4], line[5])
                callsList.append(call)
        return callsList

    @staticmethod
    def callsToCsv(callsList, outputFile):
        all = []
        for i in callsList:
            all.append(i.__dict__.values())
        with open(outputFile, 'w', newline="") as file:
            csvWriter = csv.writer(file)
            csvWriter.writerows(all)



    def __str__(self):
        return f"Name = {self.name} time stamp={self.call_time} src={self.src} dest={self.dest} status={self.status} elevindex={self.elev_index}"


if __name__ == '__main__':
    csvFile = "/Users/User/PycharmProjects/pythonProject1/Ex1_input/Ex1_calls/Calls_a.csv"
    call = Calls.loadFromCSV(csvFile)
    print(call)
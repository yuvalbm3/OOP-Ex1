import csv
import json
from typing import List

from Algo import Algo
from Building import Building
from Calls import Calls


def ex1(binj: json, cList: csv, output: csv):
    building = Building.from_json(binj)
    calls_list = loadFromCSV(cList)
    output = output
    Algo.main(building, calls_list, output)


def loadFromCSV(file) -> List:
    callsList = []
    with open(file) as f:
        csv_reader = csv.reader(f)
        for column in csv_reader:
            print("1")
            call = Calls(column[0], column[1], column[2], column[3], column[4], column[5])
            print("2")
            callsList.append(call)
    return callsList


def main():
    Calls_d = "C:/Users/User/PycharmProjects/OOP_ex1/Ex1_input/Ex1_Calls/Calls_d.csv"
    Calls_c = "C:/Users/User/PycharmProjects/OOP_ex1/Ex1_input/Ex1_Calls/Calls_c.csv"
    Calls_b = "C:/Users/User/PycharmProjects/OOP_ex1/Ex1_input/Ex1_Calls/Calls_b.csv"
    Calls_a = "C:/Users/User/PycharmProjects/OOP_ex1/Ex1_input/Ex1_Calls/Calls_a.csv"
    B1 = "C:/Users/User/PycharmProjects/OOP_ex1/Ex1_input/Ex1_Buildings/B1.json"
    B2 = "C:/Users/User/PycharmProjects/OOP_ex1/Ex1_input/Ex1_Buildings/B2.json"
    B3 = "C:/Users/User/PycharmProjects/OOP_ex1/Ex1_input/Ex1_Buildings/B3.json"
    B4 = "C:/Users/User/PycharmProjects/OOP_ex1/Ex1_input/Ex1_Buildings/B4.json"
    B5 = "C:/Users/User/PycharmProjects/OOP_ex1/Ex1_input/Ex1_Buildings/B5.json"
    output = "/Users/User/PycharmProjects/OOP_ex1/output.csv"
    # ex1(B5, Calls_a, output)

if __name__ == '__main__':
    main()
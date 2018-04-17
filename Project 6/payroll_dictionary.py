# payroll_dictionary.py - PayrollData class using a dictionary

from employee import Employee
from tkinter.filedialog import askopenfilename

class PayrollData:
    def __init__(self):
        self.staff = {}
        self.pointer = -1
        self.keys = []

    def fileopen(self):
        fileName = askopenfilename()
        infile = open(fileName, "r")
        number = infile.readline()
        while number != "":
            self.staff.setdefault(number)
            name = infile.readline()[:-1]
            address = infile.readline()[:-1]
            wage, hours = infile.readline().split()
            self.staff[number] = [name, address, float(wage), float(hours)]
            number = infile.readline()
        self.keys = list(self.staff.keys())
        self.pointer = 0

    def getData(self):
        i = self.keys[self.pointer]
        if i in self.staff:
            return self.staff[i]
        else:
            return None
        
    def datanext(self):
        if self.pointer < len(self.staff)-1:
            self.pointer += 1

    def dataprevious(self):
        if self.pointer > 0:
            self.pointer -= 1


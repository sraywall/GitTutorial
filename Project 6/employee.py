# employee.py - Employee class for Fluffshuffle Electronics

class Employee:
    def __init__(self, number, name, address, wage, hours):
        self.number = number
        self.name = name
        self.address = address
        self.wage = wage
        self.hours = hours

    def calcNetPay(self):
        if self.hours <= 40:
            gross = self.hours*self.wage
            overtime = 0.0
        else:
            gross = 40.0*self.wage
            overtime = (self.hours-40.0)*self.wage*1.5
        fedTax = (gross+overtime)*.20
        stateTax = (gross+overtime)*.075
        return gross + overtime - fedTax - stateTax

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

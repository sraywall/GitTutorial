# payroll_dictionarygui.py

from tkinter import *
from payroll_dictionary1 import PayrollData

class PayrollGUI:
    def __init__(self):
        self.data = PayrollData()
        self.employee = None
        self.root = Tk()
        self.root.title("FluffShuffle Electronics")
        self.root.configure(background="gray")
        self.name = StringVar()
        self.address = StringVar()
        self.netPay = StringVar()
        self.buttonOpen = Button(self.root, text="Open", command=self.fileopen)
        self.buttonOpen.grid(row=0, column=0, padx=10, pady=10)
        Label(self.root, text="Name").grid(row=1, column=0, padx=10, pady=10)
        self.boxName = Entry(self.root, textvariable=self.name, width=25)
        self.boxName.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        Label(self.root, text="Address").grid(row=2, column=0, padx=10, pady=10)
        self.boxAddress = Entry(self.root, textvariable=self.address, width=25)
        self.boxAddress.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
        Label(self.root, text="Net Pay").grid(row=3, column=1, padx=10, pady=10)
        self.boxNetPay = Entry(self.root, textvariable=self.netPay)
        self.boxNetPay.grid(row=3, column=2, padx=10, pady=10)
        self.buttonPrevious = Button(self.root, text="Previous", command=self.dataprevious)
        self.buttonPrevious.grid(row=4, column=0, padx=10, pady=10)
        self.buttonNext = Button(self.root, text="Next", command=self.datanext)
        self.buttonNext.grid(row=4, column=2, padx=10, pady=10)

    def fileopen(self):
        self.data.fileopen()
        self.setData()

    def setData(self):
        employee = self.data.getData()
        self.name.set(employee["name"])
        self.address.set(employee["address"])
        netPay = self.calcNetPay(employee["wage"], employee["hours"])
        self.netPay.set("${:.2f}".format(netPay))

    def calcNetPay(self, wage, hours):
        if hours <= 40.0:
            straightPay = wage*hours
            overtimePay = 0.0
        else:
            straightPay = wage*40.0
            overtimePay = 1.5*wage*(hours-40.0)
        tax = (straightPay+overtimePay)*.275
        return straightPay+overtimePay-tax

    def dataprevious(self):
        self.data.dataprevious()
        self.setData()

    def datanext(self):
        self.data.datanext()
        self.setData()

def main():
    gui = PayrollGUI()

main()

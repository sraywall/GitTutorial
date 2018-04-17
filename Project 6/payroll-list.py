# payroll.py

from tkinter import *
from tkinter.filedialog import askopenfilename

pointer = -1
staff = []
root = Tk()
name = StringVar()
address = StringVar()
netPay = StringVar()

def main():
    global root, name, address, netPay
    employee = []
    root.title("FluffShuffle Electronics")
    root.configure(background="gray")
    buttonOpen = Button(root, text="Open", command=fileopen)
    buttonOpen.grid(row=0, column=0, padx=10, pady=10)
    Label(root, text="Name").grid(row=1, column=0, padx=10, pady=10)
    boxName = Entry(root, textvariable=name, width=25)
    boxName.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    Label(root, text="Address").grid(row=2, column=0, padx=10, pady=10)
    boxAddress = Entry(root, textvariable=address, width=25)
    boxAddress.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
    Label(root, text="Net Pay").grid(row=3, column=1, padx=10, pady=10)
    boxNetPay = Entry(root, textvariable=netPay)
    boxNetPay.grid(row=3, column=2, padx=10, pady=10)
    buttonPrevious = Button(root, text="Previous", command=dataprevious)
    buttonPrevious.grid(row=4, column=0, padx=10, pady=10)
    buttonNext = Button(root, text="Next", command=datanext)
    buttonNext.grid(row=4, column=2, padx=10, pady=10)

def fileopen():
    global staff
    fileName = askopenfilename()
    infile = open(fileName, "r")
    number = infile.readline()
    while number != "":
        name = infile.readline()[:-1]
        address = infile.readline()[:-1]
        wage, hours = infile.readline().split()
        wage, hours = float(wage), float(hours)
        staff.append([number, name, address, wage, hours])
        number = infile.readline()
    setData(0)

def setData(pointer):
    global staff
    i = pointer
    if 0 <= i < len(staff):
        employee = staff[i]
    else:
        employee = None
    name.set(employee[1])
    address.set(employee[2])
    netPay.set(calcNetPay(employee))

def calcNetPay(employee):
    hours, wage = employee[4], employee[3]
    if hours <= 40:
        gross = hours*wage
        overtime = 0.0
    else:
        gross = 40.0*wage
        overtime = (hours-40.0)*wage*1.5
    fedTax = (gross+overtime)*.20
    stateTax = (gross+overtime)*.075
    return gross + overtime - fedTax - stateTax

def datanext():
    global pointer, staff
    if pointer < len(staff)-1:
        pointer += 1
    setData(pointer)

def dataprevious():
    global pointer
    if pointer > 0:
        pointer -= 1
    setData(pointer)

main()

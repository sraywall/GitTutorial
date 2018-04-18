#payroll_shuffle.py
from tkinter import *
from tkinter.filedialog import askopenfilename
class PayrollGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("FluffShuffle Electronics")
        self.root.configure(background="gray")
        self.name = StringVar()
        self.address = StringVar()
        self.netPay = StringVar()
        self.buttonOpen = Button(self.root, text="Open", command=self.openfile)
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
        self.buttonNext = Button(self.root, text="Next", command=self.nextemployee)
        self.buttonNext.grid(row=4, column=2, padx=10, pady=10)
        self.current = 0

    def setfields(self,employee):
        self.name.set(employee['name'])
        self.address.set(employee['address'])
        self.netPay.set(self.calc_salary(employee))
        
    def openfile(self):
        self.employees = []
        self.current = 0
        filename = askopenfilename()
        ifile = open(filename)
        line = ifile.readline()
        while line != "":
            number = line.strip()
            name = ifile.readline().strip()
            address = ifile.readline().strip()
            line = ifile.readline().strip().split()
            hourly = line[0]
            hours = line[1]
            line = ifile.readline().strip()
            employee = {"number":number,
                    "name":name,
                    "address":address,
                    "hourly":hourly,
                    "hours":hours}
            self.employees.append(employee)
        ifile.close()
        self.setfields(self.employees[self.current])

    def nextemployee(self):
        if self.current < len(self.employees) - 1:
            self.current += 1
        self.setfields(self.employees[self.current])

    def calc_salary(self,employee):
        hours = float(employee["hours"])
        hourly = float(employee["hourly"])
        gross = hours * hourly
        net = gross -  gross * .2 - gross * .075
        return "${:,.2f}".format(net)

if __name__ == "__main__":
    gui = PayrollGUI()
    mainloop()

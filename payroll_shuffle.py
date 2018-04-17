#payroll shuffle
from tkinter import *
from tkinter.filedialog import askopenfilename

employees = []
current = 0

def calc_salary(employee):
    hours = float(employee["hours"])
    hourly = float(employee["hourly"])
    return hours * hourly

def openfile():
    fileName = askopenfilename()
    ifile = open(fileName)
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
        global employees
        employees.append(employee)
    ifile.close()
   



def main():
    root = Tk()
    root.title("FluffShuffle Electronics")
    root.configure(background="gray")
    name = StringVar()
    address = StringVar()
    netPay = StringVar()

    def nextemployee(name=name,address=address,netPay=netPay):
        print("next!")
        pass
        global employees,current
        name.set(employees[current]["name"])
        address.set(employees[current]["address"])
        netPay.set(calc_salary(employees[current]))
        current += 1
    buttonOpen = Button(root, text="Open", command=openfile)
    buttonOpen.grid(row=0, column=0, padx=10, pady=10)
    Label(root, text="Name").grid(row=1, column=0, padx=10, pady=10)
    name = StringVar(root)
    address = StringVar(root)
    netPay = StringVar(root)
    boxName = Entry(root, textvariable=name, width=25)
    boxName.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    Label(root, text="Address").grid(row=2, column=0, padx=10, pady=10)
    boxAddress = Entry(root, textvariable=address, width=25)
    boxAddress.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
    Label(root, text="Net Pay").grid(row=3, column=1, padx=10, pady=10)
    boxNetPay = Entry(root, textvariable=netPay)
    boxNetPay.grid(row=3, column=2, padx=10, pady=10)
    buttonNext = Button(root, text="Next", command=nextemployee)
    buttonNext.grid(row=4, column=2, padx=10, pady=10)
    root.mainloop()



if __name__ == "__main__":
    main()

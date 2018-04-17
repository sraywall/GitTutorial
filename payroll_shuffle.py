#payroll shuffle
from tkinter import *
from payrollgui import PayrollGUI 


def calc_salary(employee):
    hours = float(employee["hours"])
    hourly = float(employee["hourly"])
    gross = hours * hourly
    return gross -  gross * .2 - gross * .075

  



def main():
    gui = PayrollGUI()
    mainloop()



if __name__ == "__main__":
    main()

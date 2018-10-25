##The purpose of this program is to track and save all data from Matamoras' garbage
##pickup duties, and determine what the approximate cost is to each taxable unit. 
##Behold... THE GARBAGE TRACKER!!!


from time import sleep as wait
import datetime
now = datetime.datetime.today()



def add_report():
    """Writes a new, single-line report to the reports.txt file"""
    print("--- Adding A New Report ---")
    wait(0.2)
    try:
        with open("reports.txt", "r") as reports:
            count = sum(1 for line in reports)
        day_num = count
    except FileNotFoundError:
        print("Error: The reports.txt file was not found ...")
        return
    
    ask_dater = str(input("Use today's date? y/n: "))
    if ask_dater == "y" or ask_dater == "Y":
        dater = 1
    elif ask_dater == "n" or ask_dater == "N":
        dater = 2
    else:
        print("Invalid input ...")
        return

    try:
        tons = float(input("Enter total tonnage: "))
    except ValueError:
        print("Invalid input ...")
        return
    try:
        hours = float(input("Enter total amount of hours worked: "))
    except ValueError:
        print("Invalid input ...")
        return
    try:
        fuel = float(input("Enter total gallons of diesel needed for refuel: "))
    except ValueError:
        print("Invalid input ...")
        return
    try:
        parts = float(input("Enter total cost of all parts/maintenance on the truck: "))
    except ValueError:
        print("Invalid input ...")
        return
    try:
        with open("reports.txt", "a") as reports:
            reports.write("\nDay%s " % day_num)
            if dater == 1:
                reports.write(str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " ")
            elif dater == 2:
                month = str(input("Enter month number: "))
                day = str(input("Enter day of the month: "))
                year = str(input("Enter the year: "))
                reports.write(month + "/" + day + "/" + year + " ")
            reports.write(str(tons) + "tons" + " " + str(hours) + "hours" + " " + str(fuel) + "gallons" + " " + "$" + str(parts) + "in parts/maintenance")
        refresh_totals(tons, hours, fuel, parts)
        print("--- New Report Added ---")
    except FileNotFoundError:
        print("Error: the reports.txt file was not found ...")
        return
    wait(1)



def refresh_totals(tons, hours, fuel, parts):
    """When a new report is added with the add_report() function, that function calls
    this one, in order to update total amounts in the totals.txt file"""
    try:
        with open("totals.txt", "r") as totals:
            for item, line in enumerate(totals):
                if item == 0:
                    old_tons = line
                    old_tons = float(old_tons)
                elif item == 1:
                    old_hours = line
                    old_hours = float(old_hours)
                elif item == 2:
                    old_fuel = line
                    old_fuel = float(old_fuel)
                elif item == 3:
                    old_parts = line
                    old_parts = float(old_parts)
        new_tons = str(old_tons + tons)
        new_hours = str(old_hours + hours)
        new_fuel = str(old_fuel + fuel)
        new_parts = str(old_parts + parts)
    except FileNotFoundError:
        print("Error: The totals.txt file was not found ...")
        return

    try:
        with open("totals.txt", "w") as totals:
            totals.write(new_tons + "\n" + new_hours + "\n" + new_fuel + "\n" + new_parts)
    except FileNotFoundError:
        print("Error: The totals.txt file was not found ...")
        return



def print_totals():
    """Read all total numbers in the totals.txt file and print them to the console window"""
    wait(0.3)
    print("--- Current Totals ---")
    wait(0.3)
    try:
        with open("totals.txt", "r") as totals:
            for item, line in enumerate(totals):
                wait(0.2)
                if item == 0:
                    print("Tonnage: " + line)
                elif item == 1:
                    print("Hours: " + line)
                elif item == 2:
                    print("Fuel: " + line)
                elif item == 3:
                    print("Maintenance costs: $" + line)
    except FileNotFoundError:
        print("Error: The totals.txt file was not found ...")
        return



def average_cost():
    """Determines the cost to each taxable unit, given all data entered, Milford covers 40% of the total cost"""
    taxpayers = 957
    fuel_cost = float(input("Enter average price of fuel per gallon: "))
    tipping_fee = 86
    try:
        with open("totals.txt", "r") as totals:
            for item, line in enumerate(totals):
                if item == 0:
                    tonnage = float(line)
                elif item == 1:
                    hours = float(line)
                elif item == 2:
                    fuel = float(line)
                elif item == 3:
                    maintenance = float(line)
    except FileNotFoundError:
        print("Error: The totals.txt file was not found ...")
        return

    grand_total = (tipping_fee * tonnage) + (hours * 14) + (fuel * fuel_cost) + (maintenance * 0.60)
    print("Total cost: $%.2f" % grand_total)
    final_total = grand_total / taxpayers
    wait(0.5)
    print("Total cost per taxable unit: $%.2f" % final_total)
    return final_total



def cost_per_week():
    try:
        with open("reports.txt", "r") as reports:
            count = sum(1 for line in reports) - 1
        wait(0.5)
        print("Pickup Days: %s" % count)
        wait(0.5)
        final_total = average_cost()
        per_week = final_total / (count / 2)
        print("Average cost per week: $%.2f" % per_week)
    except FileNotFoundError:
        print("Error: The reports.txt file was not found ...")
        return


    
def mainloop(tracker):
    """Provides menu features, and keeps program running until user chooses to close"""
    print("Welcome To The Garbage Tracker!")
    print("--- created by ---")
    print("Roger Howard, 2018")
    userans = ""
    while tracker == True:
        wait(0.2)
        print("------------")
        wait(0.2)
        userans = str(input("Enter 1 to check totals, 2 to add a report, 3 to check taxpayer cost, x to close: "))
        if userans == "1":
            print_totals()
        elif userans == "2":
            add_report()
        elif userans == "3":
            wait(0.5)
            userans = str(input("Enter 1 to check total cost, enter 2 to check average cost per week: "))
            if userans == "1":
                average_cost()
            elif userans == "2":
                cost_per_week()
            else:
                print("--- Invalid Input ---")
        elif userans == "x" or userans == "X":
            print("--- Closing, Thanks For Using My Tracker ...")
            print("---    :)    ---")
            wait(3)
            tracker = False
        else:
            print("--- Invalid Input ---")



tracker = True
mainloop(tracker)

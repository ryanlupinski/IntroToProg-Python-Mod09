# --------------------------------------------------------------------------- #
# Title: Assignment 09
# Description: Employee database modifier main script
# ChangeLog (Who,When,What):
# RLupinski,03.12.2022
#    - initialize script
# --------------------------------------------------------------------------- #
# Import Modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
    from IOClasses import IOhold
else:
    raise Exception("This file was not created to be imported")

# Data  ---------------------------------------------------- #
strFileName = "EmployeeData.txt"
lstEmployeeList = []
strChoice = "0"
# Data  ---------------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
data = Fp.read_data_from_file(strFileName)  # load data from file into data list var
for row in data:        # for each row in data list var, call Emp class in DataClasses Module
    lstEmployeeList.append(Emp(row[0], row[1], row[2].strip()))  # append list w/ employee objects

while True:
    Eio.print_menu_items()  # Show user a menu of options
    strChoice = Eio.input_menu_options()    # Gets user's menu option choice

    if strChoice == "1":
        Eio.print_current_list_items(lstEmployeeList)  # Show user current data in the list of employee objects
        IOhold.input_press_to_continue()  # hold for user
    elif strChoice == "2":
        newData = Eio.input_employee_data()     # Let user add data to the list of employee objects
        lstEmployeeList.append(newData)         # append list w/ new employee object
        IOhold.input_press_to_continue()  # hold for user
    elif strChoice == "3":      # let user save data to file
        strChoice = input("Do you want to save the Employee List to the file?\n"
                          "Continue: (y/n)")  # option to abort saving to file
        if strChoice == 'y':
            Fp.save_data_to_file(strFileName, lstEmployeeList)   # let user save current data to file
        else:
            print("Save aborted")
        IOhold.input_press_to_continue()  # hold for user
    elif strChoice == "4":      # Let user exit program
        strChoice = input("WARNING: EXITING PROGRAM. UNSAVED DATA WILL BE LOST\n"
                          "Continue: (y/n)")  # option to abort exiting program
        if strChoice == 'y':
            print("Goodbye")
            break
    else:
        print("Must choose options 1 - 4")
        IOhold.input_press_to_continue()    # hold for user
# Main Body of Script  ---------------------------------------------------- #

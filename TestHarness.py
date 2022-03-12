# --------------------------------------------------------------------------- #
# Title: Assignment 09
# Description: Test harness script
# ChangeLog (Who,When,What):
# RLupinski,03.12.2022
#    - initialize script, change import listings to modules
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "Larry", "David")
objP2 = Emp(2, "Jerry", "Seinfeld")
lstTable = [objP1, objP2]
# for row in lstTable:
#     print(row.to_string(), type(row))

# Test processing module
Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())

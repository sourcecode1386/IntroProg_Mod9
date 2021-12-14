# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Nick Soldano,12/1//2021,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# <Nick Soldano,<12/11/2021>,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    from DataClasses import Employee as Emp  # data classes
    from ProcessingClasses import FileProcessor as p # file processing class
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
strFileName = 'EmployeeData.txt'


try:
    lstOfEmployeeObjects = p.read_data_from_file(strFileName)
    lstOfEmployeeObjects.clear()
    for line in lstOfEmployeeObjects:
        lstOfEmployeeObjects.append(Emp(line[0], line[1], line[2].strip()))
    for row in lstOfEmployeeObjects:
        print(row.to_string(), type(row))


    while True:
        Eio.print_menu_items()
        strChoice = Eio.input_menu_options()
        if  strChoice.strip() == '1':
            Eio.print_current_list_items(lstOfEmployeeObjects)
        elif strChoice.strip() == '2':
            lstOfEmployeeObjects.append(Eio.input_employee_data())
        elif strChoice.strip() == '3':
            p.save_data_to_file('EmployeeData.txt', lstOfEmployeeObjects)
            print('File Saved!')
        elif strChoice.strip() == '4':
           break
        else:
            print("Invalid choice")

except Exception as e:
    print("There was an error! Check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')


# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program


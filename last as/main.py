from facalitiesclasses import Facility

print("Welcome to Alberta Hospital (AH) Managment system")
no = input(
    "Select from the following options, or select 0 to stop: \n1-Doctors\n2-Facilities\n3- Laboratories\n4-Patients\n")
if no == '2':
    i = 0
    while i != 3:
        opt = input("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n")
        if opt == '1':
            Facility.displayFacilities(Facility)
            print("Back to the prevoius Menu")
        if opt == '2':
            Facility.addFacility(Facility)
            print("Back to the prevoius Menu")
        if opt == '3':
            print("Back to the prevoius Menu")
            quit()
else:
    quit()

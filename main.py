#Made by Gurmaher Pal Singh, Nishant and Parth

class Doctor:
    
    def __init__(self):
        pass
# now lets define a function to format the information of doctors        
    def formatDrInfo(self,doctor_list):
        format_doctor=''
        for doctor in doctor_list:
            doctor=doctor[0]+'_'+doctor[1]+'_'+doctor[2]+'_'+doctor[3]+'_'+doctor[4]+'_'+doctor[5]+'\n'
            format_doctor+=doctor
        return format_doctor
# function to read data from file about doctors and fill it into our object list        
    def readDoctorsFile(self):
        doctor_list=[]
        with open ('doctors.txt','r') as af:
            for row in af:
                row = row.rstrip('\n')
                row=row.split('_')
                doctor_list.append(row)
        return doctor_list
# function to add new information to the doctors file 
    def addDrToFile(self,doctor_list):
        self.id=input('Enter the doctor’s ID:\n')
        self.name=input('Enter the doctor’s name:\n')
        self.speciality=input('Enter the doctor’s specility:\n')
        self.timing=input('Enter the doctor’s timing (e.g., 7am-10pm):\n')
        self.qualification=input('Enter the doctor’s qualification:\n')
        self.room_number=input('Enter the doctor’s room number:\n')
        new_doctor=[self.id,self.name,self.speciality,self.timing,self.qualification,self.room_number]
        doctor_list.append(new_doctor)
        return doctor_list
#function to enter list of data onto the file    
    def writeListOfDoctorsToFile(self,format_doctor):
        with open('doctors.txt','w') as lf:
            lf.write(format_doctor)
        pass
    
#looks up the id of doctor in records and shows details of matching data  
    def searchDoctorById(self,doctor_list):
        id= input('\nEnter the doctor’s ID:\n')
        for doctor in doctor_list:
            if id == doctor[0]:
                print('\nId'.ljust(15),'Name'.ljust(15),'Speciality'.ljust(15),'Timing'.ljust(15),'Qualification'.ljust(15),'Room Number\n'.ljust(15))
                print(doctor[0].ljust(15),doctor[1].ljust(15),doctor[2].ljust(15),doctor[3].ljust(15),doctor[4].ljust(15),doctor[5].ljust(15))
                return doctor
        print("Can't find the doctor with the same ID on the system")
        return False
#looks up the name of the doctor in records and shows details of matching data        
    def searchDoctorByName(self,doctor_list):
        doc_name=input('\nEnter the doctor’s name:\n\n')
        for doctor in doctor_list:
            if doc_name == doctor[1]:
                print('\nId'.ljust(15),'Name'.ljust(15),'Speciality'.ljust(15),'Timing'.ljust(15),'Qualification'.ljust(15),'Room Number\n'.ljust(15))
                print(doctor[0].ljust(15),doctor[1].ljust(15),doctor[2].ljust(15),doctor[3].ljust(15),doctor[4].ljust(15),doctor[5].ljust(15))
                return doctor
        print("Can't find the doctor with the same name on the system")
        return False
#function to change/edit the information of doctors         
    def editDoctorInfo(self,doctor_list):
        id_no= input('\nPlease enter the id of the doctor that you want to edit their information:\n\n')
        for doctor in doctor_list:
            if id_no == doctor[0]:
                doctor[1]=input('Enter new Name: \n')
                doctor[2]=input('Enter new Specilist in:\n')
                doctor[3]=input('Enter new Timing: (e.g., 7am-10pm):\n')
                doctor[4]=input('Enter new Qualification: \n')
                doctor[5]=input('Enter new Room number: \n')
                index=doctor_list.index(doctor)
                doctor_list[index]=doctor
                return doctor_list
        print("Can't find the doctor with the same ID on the system")
        pass
#displays doctor information   
    def displayDoctorsList(self,doctor_list):
        for doctor in doctor_list:
            print(doctor[0].ljust(15),doctor[1].ljust(15),doctor[2].ljust(15),doctor[3].ljust(15),doctor[4].ljust(15),doctor[5].ljust(15))
        pass
        

class facility():
    def __init__(self):
        self.txt=[]
        with open("facilities.txt", "r") as fo:
            lines=fo.readlines()
            for line in lines:
                self.txt.append(line.split("\n")[0])
# add name to facilities
    def addFacility(self,name):
        self.txt.append(name)
#displays a list of facilities
    def displayFacilities(self):
        for name in self.txt:
            print(name)
        print('Back to the prevoius Menu')    
#adds new facilities in the facilities file
    def writeListOffacilitiesToFile(self):
        with open("facilities.txt", "w") as fo:
            for name in self.txt:
                fo.write(name+"\n")
class Patient:
    def __init__(self,pid,name,disease,gender,age):
        self.pid =pid
        self.name=name
        self.disease = disease
        self.gender = gender
        self.age = age
#formats patient info 
    def formatPatientInfo(self): 
        return "%s_%s_%s_%s_%s"%(self.pid,self.name,self.disease,self.gender,self.age)
#takes input for patient info   
    def enterPatientInfo(self): 
        self.pid = input("Enter the patient ID: \n")
        self.name = input("Enter the patient's name: \n")
        self.disease = input("Enter the patient's disease: \n")
        self.gender = input("Enter the patient's gender: \n")
        self.age = input("Enter the patient's age: \n")
#reads the data from patients file 
    def readPatientsFile(self):
        file = open("patients.txt","r")
        patient_file = file.readlines() 
        for i in patient_file:
            patient_file[patient_file.index(i)] = i.strip("\n")
        file.close()
        return patient_file
#looks for patient data from id
    def searchPatientById(self): 
        id = input("Enter the patient id you want to search:")
        patientsInfo_list = self.readPatientsFile()
        results = 0
        found = []
        for each_string in patientsInfo_list:
            if id == each_string[:len(id)]:
                results += 1
                found.append(each_string)
    
        if results <1:
            print("The patient ID entered is not found.")
        else:
            print("The following patient(s) are/is found:")
            for each_item in found:
                print(each_item.replace("_","\t"))
#shows info about the patient           
    def displayPatientInfo(self):
            print(self.formatPatientInfo.replace("_","\t"))
    def editPatientInfo(self):
        id = input("Please enter the id of the patient that you want to edit their information: \n")
        listpatient = self.readPatientsFile()
        list_of_patientlist = []
        for each_string in listpatient:
            if id ==each_string[:len(id)]:
                sublist = each_string.split("_")
                sublist[1] = input("Enter the patient's new name: \n")
                sublist[2]= input("Enter the patient's new disease: \n")
                sublist[3]= input("Enter the patient's new gender: \n")
                sublist[4]= input("Enter the patient's new age: \n")
                list_of_patientlist.append(sublist)
            else:
                sublist = each_string.split("_")
                list_of_patientlist.append(sublist)
        
#making a new file
        file = open("patients.txt","w")
        for each_sublist in list_of_patientlist:
            file = open("patients.txt","a")
            file.write("%s_%s_%s_%s_%s"%(each_sublist[0],each_sublist[1],each_sublist[2],each_sublist[3],each_sublist[4]) + "\n")
            file.close()
# shows the list of  patients    
    def displayPatientsList(self):
        patient_file = self.readPatientsFile()
        for each_list in patient_file:
            print(each_list.replace("_","\t"))
# writes list of patients into file patiens.txt
    def writeListOfPatientsToFile(self,list_of_patients):
        file = open("patients.txt","a")
        for each_patient in list_of_patients:
            file.write("\n" + each_patient.formatPatientInfo())
            each_patient.formatPatientInfo()
    
    def addPatientToFile(self):
        self.enterPatientInfo()
        file = open("patients.txt","a")
        file.write("\n"+self.formatPatientInfo())
        file.close

class Laboratory:
    def __init__(self,name,cost):
        self.lab_name = name
        self.lab_cost = cost

    def addLabToFile(self):
        self.enterLaboratoryInfo()
        flab = open("laboratories.txt","a")
        flab.write(self.formatLabInfo()+"\n")
        flab.close()

    def writeListOfLabsToFile(self,list_of_labs):
        flab = open("laboratories.txt","a")
        for each_lab in list_of_labs:
            flab.write("\n" + each_lab.formatLabInfo())
            

    def displayLabsList(self):
        flab = open("laboratories.txt","r")
        lab_list = []

        for each_line in flab:
            new_list = each_line.split("_")
            lab_list.append([new_list[0],new_list[1].strip()])
        flab.close()
        
        for i in lab_list:
            print("%s\t\t%s"%(i[0],i[1]))
    
    def formatLabInfo(self):
        lab_info = "%s_%s"%(self.lab_name,self.lab_cost)
        return lab_info
    
    def enterLaboratoryInfo(self):
        self.lab_name = input("Enter the name of the Laboratory:\n")
        self.lab_cost = input("Enter the cost of the Laboratory:\n")
    
    def readLaboratoriesFile(self):
        flab = open("laboratories.txt","r")
        lab_obj_list = []
        
        for each_line in flab:
            line_list = each_line.split("_")
            new_lab = Laboratory(line_list[0],line_list[1])
            lab_obj_list.append(new_lab)
        
def laboratories():
    lab=Laboratory("name",0)
    while True:
        print("\nLaboratories Menu:")
        print("1 - Display laboratories list")
        print("2 - Add laboratory")
        print("3 - Back to the Main Menu\n")            
        choose3 = input()
        if choose3 == "1":
            lab.displayLabsList()
        elif choose3 == "2":
            lab.addLabToFile()
        elif choose3 == "3":
            break
        else:
            print('\nYou input a wrong number. Please try it again.\n')
            print('\nBack to the previous Menu\n')
            break

def patients():
    p = Patient(00,"PatientX","Cold","","22")
    while True:
        print("\nPatients Menu:")
        print("1 - Display patients list")
        print("2 - Search patient by ID")
        print("3 - Add patient")
        print("4 - Edit patient info")
        print("5 - Back to the Main Menu\n")
        choose4 = input()
        if choose4 =="1":
            p.displayPatientsList()
        elif choose4 =="2":
            p.searchPatientById()
        elif choose4 == "3":
            p.addPatientToFile()
        elif choose4 == "4":
            p.editPatientInfo()
        elif choose4 == "5":
            break
        else:
            print('\nYou input a wrong number. Please try it again.\n')
            print('\nBack to the previous Menu\n')
            break
def doctors():
    while True:
        dt=Doctor()
        doctor_list=dt.readDoctorsFile()
        no=input('\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n')
        if no=='1':
            dt.displayDoctorsList(doctor_list)
            print('\nBack to the prevoius Menu\n')
        elif no=='2':
            dt.searchDoctorById(doctor_list)
            print('\nBack to the prevoius Menu\n')
        elif no=='3':
            dt.searchDoctorByName(doctor_list)
            print('\nBack to the prevoius Menu\n')
        elif no=='4':
            new_doctorList=dt.addDrToFile(doctor_list)
            format_doctor=dt.formatDrInfo(new_doctorList)
            dt.writeListOfDoctorsToFile(format_doctor)
            print('\nBack to the prevoius Menu\n')
        elif no=='5':
            new_doctorList=dt.editDoctorInfo(doctor_list)
            format_doctor=dt.formatDrInfo(new_doctorList)
            dt.writeListOfDoctorsToFile(format_doctor)
            print('\nBack to the prevoius Menu\n')
        elif no=='6':
            print('\nBack to the prevoius Menu\n')
            break
        else:
            print('\nYou input a wrong number. Please try it again.\n')
            print('\nBack to the prevoius Menu\n')
            break

def facilitys():
    of=facility()
    while True:
        print("\nFacilities Menu:")
        print("1 - Display Facilities list")
        print("2 - Add Facility")
        print("3 - Back to the Main Menu\n")            
        choose2 = input()
        if choose2 == "1":
            of.displayFacilities()
        elif choose2 == "2":
            name = input("Enter Facility name:\n")
            of.addFacility(name)
            of.writeListOffacilitiesToFile()
            print('\nBack to the prevoius Menu\n')
        elif choose2 == "3":
            break
        else:
            print('\nYou input a wrong number. Please try it again.\n')
            print('\nBack to the prevoius Menu\n')
            break

        
        
#Running main program
if __name__ == '__main__':
    while True:
        print('\nWelcome to Alberta Hospital (AH) Managment system\n')
        nav1=input("Select from the following options, or select 0 to stop: \n1 - 	Doctors \n2 - 	Facilities \n3 - 	Laboratories \n4 - 	Patients\n")
        if nav1=='1':
            doctors()
        elif nav1=='2':
            facilitys()
        elif nav1=='3':
            laboratories()
        elif nav1=='4':
            patients()
        elif nav1=='0':
            break
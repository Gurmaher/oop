class Facility:
    def __init__(self, n):
        self.name = n

    def addFacility(self):
        fid = 'facilities.txt'
        with open(fid, "a") as page:
            self.name = input("Enter Facility Name:")
            page.write("\n" + self.name + "\n")

    def displayFacilities(self):
        with open('facilities.txt', "r") as page:
            for line in page:
                print(line.strip())

    def writeListOffacilitiesToFile(self, list):
        with open('facilities.txt', "w") as page:
            for line in page:
                page.write(line.name + "\n")

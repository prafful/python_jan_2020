#inheritance
#parent class
class ParentClass:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def getFname(self):
        return self.fname

    def getLname(self):
        return self.lname        

#child class
class ChildClass(ParentClass):
    
    def __init__(self, fname, lname, address):
        #using super to call contructor of parent class to set fname, lname
        super().__init__(fname, lname)
        self.address = address

    #getFName() and getLname() of Parent Class are accessible in Child Class because of inhertiance
    def getDetails(self):
        return "Name: " + self.getFname() + " " + self.getLname() + " Location: " + self.address 


cc = ChildClass("Prafful", "Daga", "Chennai")
print(cc.getDetails())
print(cc.getFname())
print(cc.getLname())
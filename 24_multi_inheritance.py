#multiple inheritance
'''
    class Father:
        code

    class Mother:
        code

    class Child(Father, Mother):
        code        



'''
#multi-level inheritance
'''
class GrandFather:
    code

class Father(GrandFather):
    code

class Child(Father):
    code        

'''
#Parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

#Parent class
class Consultant:
    def __init__(self, contractamount, duration):
        self.contractamount = contractamount   
        self.duration = duration     


#Child Class -> Project Team            
class ProjectTeamMember(Employee, Consultant):
    def __init__(self, name, salary,contractamount, duration, expertise ):
        self.expertise = expertise
        #super().__init__() is of no use here as self has two parents!
        Employee.__init__(self, name, salary)
        Consultant.__init__(self, contractamount, duration)
        print("Name: {}, Salary: {}, Duration: {}, Expertise: {}".format(self.name, self.salary, self.duration, self.expertise) )


developer = ProjectTeamMember('Prafful', 8888, 0, 4, "Game Dev")

#multi-level inheritance
#parent class
class Project:
    projectName = ""

    def getProjectDetail(self):
        print("Project detail includes:")

class Architect(Project):
    architectName = ""
    def getArchitectName(self):
        print(self.architectName)

class Developer(Architect):    
    developerName = ""
    def getDeveloperName(self):
        print(self.developerName)
        
#inherits from Developer and Architect
#MRO error will come if Srint is declared as class Sprint(Architect, Developer):
class Sprint(Developer, Architect):
    def getSprintInfo(self):
        print("Developer: ",  self.developerName)
        print("Architect: " , self.architectName)
        


sprintInstance = Sprint()   
sprintInstance.architectName = "Prafful Daga"     
sprintInstance.developerName = "MoneySingh"
sprintInstance.getProjectDetail();
sprintInstance.getSprintInfo()
print("-------MRO of Sprint Class-------")
print(Sprint.mro())

#mro
#agile is parent class
class Agile: 
   def create(self): 
      print(" class Agile") 

#dev is child of agile
# create function of agile is overridden
class Dev(Agile): 
   def create(self): 
      print(" class Dev") 

#qa is child of agile
#create function of agile is overridden
class QA(Agile): 
   def create(self): 
      print(" class QA") 

   def createOne(self):
      print(" in Create One") 

# Ordering of classes
#sprint is child to dev and qa
#mro (left to right) will decide which implementation 
# of create is called
class Sprint(Dev, QA ): 
   pass

sprint = Sprint() 
sprint.create()
sprint.createOne()
print(Sprint.mro())

#functions
'''
def funcname(parameter_list):
    pass
'''
# define the function before it is called!
def message():
    print("This is default message!")

message()    

def customMessage(message):
    print(message)

msg = input("Message: ")
customMessage(msg)

#polymorphism in python!
def screenPrint():
    print("This is default screen print message!")

screenPrint() 

def screenPrint(msg):
    print(msg)


#def screenPrint(message1, message2):
#    print(message1 , " and ", message2)


#msg1 = input("Message 1: ")
#msg2 = input("Message 2: ")


screenPrint("Polymorphism!")  
#screenPrint(msg1, msg2)





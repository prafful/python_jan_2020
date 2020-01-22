"""
try:
    execute code block 1
except expression as identifier:
    execute if code block 1 get error
else:
    execute if code bloack 1 is success!

"""
try:
    fh = open("check.txt", "w")
    print(fh.write("Hello from Exception!"))
except BaseException as exception:
    print("Error while working with file: ", exception )    
else:
    print("File operation is success!")
    fh.close()


try:
    fh = open("check.txt", "r")
    print(fh.read())
except IOError as exception:
    print("Error while working with file: ", exception )    
else:
    print("File operation is success!")
    fh.close()


try:
    fh = open("check1.txt", "r")
    print(fh.read())
except IOError as exception:
    print("In Except:" , exception)
finally:
    print("I am in finally block!")
    fh.close()

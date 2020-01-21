#file handling
"""
1.open the file -> it will return filehandle
2.use filehandle to do file operations (read, write, change attributes, delete) 
3.close the filehandle

#file open modes
r   - read only mode. offset will remain in  beginning.
rb  - read only in binary mode. offset will remain in  beginning.
r+  - read and write mode. offset will remain in  beginning.
rb+ - read and write in binary mode. offset will remain in  beginning.
w   - write mode. If  file does not exist then it will create the same. offset will remain in  beginning. 
wb  - write in binary mode. offset will remain in  beginning.
a   - append mode. file will open and offset (place to start reading/writing the file) will go at EOF.
ab  -
"""
fh = open("01.py", "r")
#file name
print(fh.name)
# check whether file is open or close
print("File is Closed : ", fh.closed)
# check mode in which file is open
print(fh.mode)
#close filehandle
print(fh.close())
# check whether file is open or close
print("File is Closed : ", fh.closed)
print("--------------------------------------------------------")
#with - use it to auto close the file after all operations
with open("02.py") as fh:
    #file name
    print(fh.name)
    # check whether file is open or close
    print("File is Closed : ", fh.closed)
    # check mode in which file is open
    print(fh.mode)
    #close filehandle
    #print(fh.close())
    # check whether file is open or close
    #print("File is Closed : ", fh.closed)
print("File is Closed : ", fh.closed)
print("--------------------------------------------------------")
#write to file!
with open("pythonwrite.txt", "w" ) as fh:
    fh.write("Hello from Python \n")
    fh.write("Second to none! \n")
    fh.write("That was fun to write to file 2!\n")
print("File is Closed : ", fh.closed) 

print("--------------------------------------------------------")
#write to file in append mode!
with open("pythonwrite.txt", "a" ) as fh:
    fh.write("Hello from Python \n")
    fh.write("Second to none! \n")
    fh.write("That was fun to write to file 2!\n")
print("File is Closed : ", fh.closed)

print("--------------------------------------------------------")
with open("pythonwrite.txt", "r") as fh:
    content = fh.readlines()
print(content)    
for eachline in content:
    print(eachline)
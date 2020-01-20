'''
while expression/condition:
    block of code
'''

startNumber = int(input("Input start number (Diff to be less than 20):"))
endNumber = int(input("Input end number (Diff to be less than 20):"))
counter = startNumber
while counter<=endNumber:
    if(endNumber - startNumber >= 20):
        break
    print(counter)
    counter +=1
else:
    print("Numbers from %d to %d printed!" % (startNumber, endNumber))

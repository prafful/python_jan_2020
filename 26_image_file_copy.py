fhr = open("1.jpg",'rb')
print("Current offset: ",  fhr.tell())
content = fhr.read()
print("Current offset: ",  fhr.tell())
print(content)
fhw = open("2.jpg", "wb")
fhw.write(content)

fhr.close()
fhw.close()

fhr = open("pythonwrite.txt",'r')
print("Current offset: ",  fhr.tell())
content = fhr.read()
print("Current offset: ",  fhr.tell())
print(content)
fhw = open("newfile.txt", "w")
fhw.write(content)

fhr.close()
fhw.close()
name1 = 'prafful'
name2 = "daga"
description = """i
                  am
                    in
                        multiple
                                 lines"""

#part 1
""" print(name1)
print(name2)
print(description)
#replace  substring
newDescription = description.replace("multiple", "more than one")
print(newDescription)


print(name1[0])  # oth psition
print(name1[-1]) # last nth positoin
print(name1[-2])    #last nth-1 position """

#part 2
print(name2[0])
 
#invalid operations 
#name2[0] = 'l'
#name2[0.1]
#del name2[0]

print(name2)

#concatenation

name3 = name1 + " " + name2 + " "
print(name3)

#string multiplication
print(name3*4)
name4 = name3*4
print(name4)

#membership operator
print('p' in name1)
print('d' in name1)

print('p' not in name1)

for alpha in name1:
    print(alpha)


#using escape sequence
test = "I am fine as \"beach\""
print(test)


#using format characters
score = 99
# Name: Prafful
# Score: 99
print("Name: %s \nScore: %d" % (name1, score))

#inbuilt functions
name3= "pRaFFul daga"
print(name3.capitalize())
print(name3.lower())
print(name3.swapcase())
print(name3.upper())
print(name3.title())
print(name4.title())
print(name4.count("prafful", 0, len(name4)-1))
name4 = name4 + " test"
print(name4)
print(name4.count(" test", 0, len(name4)))
print(name4.count("daga", 0, len(name4)-5))
print(name4.count("f", 0, len(name4)-1))
print(name4.count("a", 0, len(name4)))
print(name4.count("t", 0, len(name4)))
print(len(name4))
print(name4.count("test", 0, len(name4)))


print(name1.islower())
print(name1.isupper())

print(name3.center(40, '*'))

mydict = {}
print(type(mydict))
number_dict = {1:"one", 2:"two"}
print(number_dict)
mix_dict = {
                1:"one", 
                "location":"chennai", 
                "scores":[25, 35, 45]
            }

print(mix_dict)
print(type(mix_dict))

dictFunction = dict({1:"one", 2:"two"})
print(dictFunction)

print(dictFunction[1])
print(mix_dict["location"])
number_dict = {1:"one", 2:"two"}
number_dict[3] = "three"
print(number_dict)

number_dict.update({4:"four"})
print(number_dict)
number_dict[3] = "threethree"
print(number_dict)
number_dict.update({4:"fourfour"})
print(number_dict)

checkThis = {"1":None}
print(checkThis)
print(type(None))

print(number_dict.get(4))
print("-----------------------------")
print(number_dict.pop(4))
print(number_dict)
print("-----------------------------")
print(number_dict.popitem())
print(number_dict)
print("-----------------------------")
print(number_dict.clear())
print(number_dict)
del number_dict
#print(number_dict)


number_dict1 = {1:"one", 2:"two", 3: "three"}
number_dict2 = {1:"oneone", 4:"four"}
number_dict3 = {}
number_dict3.update(number_dict1)
number_dict3.update(number_dict2)
print(number_dict3)
print("----------------------------------")
number_dict3.update(number_dict2)
number_dict3.update(number_dict1)
print(number_dict3)
print("----------------------------------")
#unpacking operator
number_dict3 = {}
number_dict3 = { **number_dict1, **number_dict2 }
print(number_dict3)
print("----------------------------------")
#unpacking operator
number_dict3 = {}
number_dict3 = { **number_dict2, **number_dict1 }
print(number_dict3)








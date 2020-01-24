#map -> will work only on iterable/collection
#    -> it will return the list created by lambda function (parameter of map)

messages = ["Help", "Run", "Walk", "Eat", "Speak"]


mapdone = map(lambda a: '@'+a+'@', messages)

output = list(mapdone)
print(output)
print(type(output))

def doThis(a):
    return '#'+a +'#'

legacyway = map(doThis, messages)
print("---------------legacy way-----------------")
print(list(legacyway))
print("--------------map on one element in iterable------------------")
onlyone = (4,)
onlyonemap = map(lambda a: '@'+str(a)+'@', onlyone)
output = list(onlyonemap)
print(output)

########################################################
mapdone = map(lambda a: a.upper(), messages)
print(list(mapdone))
#################################################
score_python = [20, 40, 50, 10]
score_logic = [10, 50, 80, 10]
total_score_lambda = list(map(lambda n1, n2: n1+n2, score_python, score_logic))
print("Total Score Lambda: ", total_score_lambda)

def get_total_score(n1, n2):
    return n1 + n2
total_score_function = list(map(get_total_score, score_python, score_logic))
print("Total Score Function: ", total_score_function)
####################################################

score_python = [20, 40, 50, 10]
score_logic = [10, 50, 80, 10,  50, 10, 70, 60]
score_ds = [50, 40, 50, 10]
total_score_size = list(map(lambda n1, n2, n3: n1+n2+n3, score_python, score_logic, score_ds))
print("Total Score Different Size: ", total_score_size)

####################################################
def get_total_score(n1, n2, n3):
    return n1 + n2 + n3
total_score_function = list(map(get_total_score, score_python, score_logic, score_ds))
print("Total Score Function 3 arguments: ", total_score_function)



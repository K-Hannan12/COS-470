# Kaleb Hannnan
# HW3
# COS 470 at the University of Maine Orono
# Genetic Algroithm for matching to a string a ACSII chars

import random

targetString = ""
populationNum = 100
population = []
mutation_rate = 0.05

#funtion takes two partnts anc creates a child
def crossover(p1, p2):

    length = len(p1)
    ranNum = random.randint(1,length - 1)
    child = p1[:ranNum] + p2[ranNum + 1:]

    return child

def mutation(child, targetString):
    return child

def fitness(ind, targetString):
    score = 0
    for i in range(len(ind)):
        if ind[i] == targetString[i]:
            score+=1

    return score

# Take imput from terminal about what file you string is in
print("Enter File Name:", end=" ")
fileName = input()

with open(fileName, "r") as File:
    targetString = File.read()

# this might need to get replaced but for know we good
targetString = targetString.replace("\n", " ")
print(targetString)
# Get len of the string to make the correct population the correct length
lenOftarget = len(targetString)

# create population
for i in range(populationNum):
    individual = ""
    for y in range(lenOftarget):
        ranChar = chr(random.randint(0,255))
        individual += ranChar
    population.append(individual)


#For testing
#print(len(population))
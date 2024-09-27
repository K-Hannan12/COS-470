# Kaleb Hannnan
# HW3
# COS 470 at the University of Maine Orono
# Genetic Algroithm for matching to a string a ACSII chars

import random

targetString = ""
populationNum = 100
population = []

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

print(len(population))
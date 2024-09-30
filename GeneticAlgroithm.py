# Kaleb Hannnan
# HW3
# COS 470 at the University of Maine Orono
# Genetic Algroithm for matching to a string a ACSII chars

import random

targetString = ""
populationNum = 100
population = []
mutation_rate = 0.05

# Funtion takes two partnts anc creates a child
def crossover(p1, p2):

    length = len(p1)
    ranNum = random.randint(1,length - 1)
    child = p1[:ranNum] + p2[ranNum + 1:]

    return child

# Cheaks to see if a char can be mutated and if it can it will.  
# It will also only mutate the char if it dose not mach the target string.
def mutation(child, targetString):
    for i in range(len(child)):
        if child[i] != targetString[i]:
            if random.random() <= mutation_rate:
                child = child[:i] + chr(random.randint(0,255)) + child[i+1:]
    return child

# This function cheaks to see if fitness of the indavidual in the population.
def fitness(ind, targetString):
    score = 0
    for i in range(len(ind)):
        if ind[i] == targetString[i]:
            score+=1

    return score

def GeneticAlgroithm():
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
    
    #While loop to run until we match the string
    while True:
       break 
    
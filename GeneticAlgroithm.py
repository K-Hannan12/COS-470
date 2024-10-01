# Kaleb Hannnan
# HW3
# COS 470 at the University of Maine Orono
# Genetic Algroithm for matching to a string a ACSII chars

import random

# Funtion takes two partnts anc creates a child
def crossover(p1, p2):

    length = len(p1)
    ranNum = random.randint(1,length - 1)
    child = p1[:ranNum] + p2[ranNum + 1:]

    return child

# Cheaks to see if a char can be mutated and if it can it will.  
# It will also only mutate the char if it dose not mach the target string.
def mutation(child, targetString, mutation_rate):
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

# create population
def createPopulation(lenOftarget,populationNum):
    population = []
    for i in range(populationNum):
        individual = ""
        for y in range(lenOftarget):
            ranChar = chr(random.randint(0,255))
            individual += ranChar
        population.append(individual)

    return population

# This function selects parents to make children 
def selection(population, avgFitness):
    eligibleparents = []
    for i in population:
        if fitness(i) >= avgFitness:
            eligibleparents.append(i)
    if len(eligibleparents) < 2:
        p1 = random.choice(population)
        p2 = random.choice(population)
        while p1 == p2:
            p2 = random.choice(population)
    else:
        p1 = random.choice(eligibleparents)
        p2 = random.choice(eligibleparents)
        while p1 == p2:
            p2 = random.choice(eligibleparents)
    return p1, p2
             

def GeneticAlgroithm():

    targetString = ""
    populationNum = 100
    mutation_rate = 0.05

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

    population = createPopulation(lenOftarget, populationNum)
    
    #While loop to run until we match the string
    while True:
       break 
    
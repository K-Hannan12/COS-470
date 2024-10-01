# Kaleb Hannnan
# HW3
# COS 470 at the University of Maine Orono
# Genetic Algroithm for matching a string of ACSII chars

import random

# Funtion takes two partnts anc creates a child
def crossover(p1, p2):
    length = len(p1)
    ranNum = random.randint(1,length - 1)
    child = p1[:ranNum] + p2[ranNum:]

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
    score = 0.0
    for i in range(len(ind)):
        if ind[i] == targetString[i]:
            score+=1.0

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
def selection(population, avgFitness,fitnessPerInd):
    eligibleparents = []
    for i in range(len(fitnessPerInd)):
        if fitnessPerInd[i] >= avgFitness:
            eligibleparents.append(population[i])
    if len(eligibleparents) < 2:
        p1 = random.choice(population)
        p2 = random.choice(population)
    else:
        p1 = random.choice(eligibleparents)
        p2 = random.choice(eligibleparents)
    return p1, p2
             

def GeneticAlgroithm():
    iterations = 0
    targetString = ""
    POPULATION_SIZE = 100
    MUTATION_RATE = 0.05

    # Take imput from terminal about what file you string is in
    print("Enter File Name:", end=" ")
    fileName = input()

    with open(fileName, "r") as File:
        targetString = File.read()

    # Get len of the string to make the correct population the correct length
    lenOftarget = len(targetString)

    population = createPopulation(lenOftarget, POPULATION_SIZE)
    
    population.sort(key = lambda ind: fitness(ind, targetString), reverse = True)

    if population[0] == targetString:
        print ("Mach found: " + population[0])
        return 

    #While loop to run until we match the string
    while True:
        newPopulation = []
        fitnessPerInd = []
        totalFitness = 0.0

        #calculate the avg fitness of the population
        for ind in population:
            fit = fitness(ind,targetString)
            totalFitness += fit
            fitnessPerInd.append(fit)
            if totalFitness !=0:
                avgFitness = totalFitness / POPULATION_SIZE
            else:
                avgFitness = 0.0
        
        #Create new population 
        i = 0
        while i < POPULATION_SIZE:
            p1,p2 = selection(population,avgFitness,fitnessPerInd)
            child = crossover(p1, p2)
            child = mutation(child,targetString,MUTATION_RATE)
            newPopulation.append(child)
            i+=1
        
        population = newPopulation

        population.sort(key = lambda ind: fitness(ind, targetString), reverse = True)

        if population[0] == targetString:
            print("Match Found in Iteration #" + str(iterations) + ":\n" + population[0] + "\n\n")
            return
        else:
            #print("Best Match in Iteration " + str(iterations) + ": \n" + population[0] + "\n")
            print("Best Match in Iteration #" + str(iterations) + " has fitness of " + str((fitness(population[0],targetString)/ len(targetString) * 100))+ "%\n\n")
            iterations += 1

GeneticAlgroithm()
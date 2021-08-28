#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 08:43:41 2021

@author: Taylor Emmons
"""


import random
import math

import time;

def selection(population, a, b, c, sols):
    
    #Closer to zero is better
    scores = [];
    
    for pheno in population:
        score = a*pheno[0] + b*pheno[1] + pheno[0]*pheno[1];
        score = abs(score - c);
        
        scores.append(score);
        
    
    scoreCard = list(zip(scores, population));
    
    scoreCard.sort();
    scoreCard = scoreCard[0:len(scoreCard)//2];
    

    for pheno in scoreCard:
        if pheno[0] == 0:
            p = pheno[1].copy();
            sols.append(p);

            
    score, population = zip(*scoreCard);
    
    return list(population);


def crossOver(population):
    random.shuffle(population);
    
    l = len(population)//2;
    
    parentsA = population[0:l];
    parentsB = population[l:];
    children = [];
    
    for i in range(l):
        x1, y1 = parentsA[i][0:1], parentsA[i][1:];
        x2, y2 = parentsB[i][0:1], parentsB[i][1:];
        
        childA = x1 + y2;
        childB = x2 + y1;

        children.append(childA);
        children.append(childB);
        
        
    return children;


def mutation(population, chance):
    
    for pheno in population:
        p = random.uniform(0, 1);
        
        if p < chance:
            pheno[0] += 1;
            pheno[1] -= 1;

    return population;


def factors(a, b, x, y):   
    return (x + b, y + a);


def decompose(n):
    
    a = int(math.sqrt(n))
    b = int(n/a);
    c = n % a;
    
    return a, b, c;


def geneticFactor(n, popSize, generations, mutationChance, timeout=1):

    t0 = 0;
    t1 = 0;
    
    a, b, c = decompose(n);  
    searchRange = int(math.sqrt(n))
    population = [[random.randint(-searchRange, searchRange) for j in range(2)] for i in range(popSize)]
    solutions = [];
    
    
    t0 = time.time();
    
    while(len(solutions) < 1):
        
        population = selection(population, a, b, c, solutions);
        population += crossOver(population);
        population = mutation(population, mutationChance);
        
        t1 = time.time();
        
        if t1 - t0 > timeout:
            print("Timeout reached.");
            break;
    
    sols = list(set(map(tuple, solutions)));
    for solution in sols:
        print(factors(a, b,  solution[0], solution[1]));


    

#The number to factor
#   (It really doesn't like primes)


n = 123456

populationSize = 8;
generations = 1000;
mutationChance = .35;



t0 = time.time();

geneticFactor(n, populationSize, generations, mutationChance, 10);

print(time.time() - t0);




    
    
    
    
    
    
    
    
    
    
    
    
    
    




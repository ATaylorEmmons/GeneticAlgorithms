#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 08:10:21 2021

@author: Taylor Emmons
"""

import random

#____________Interface

#          Weight, Value
Objects = [(10, 60),
           (20, 100),
           (30, 120)]


weightLimit = 50
populationSize = 8;



#____________Internal

class Phenotype:
    
    def __init__(self, traits = []):
        weight = 0;
        value = 0;
        
        if(len(traits) == 0):
            traits = [random.randint(0, 1) for k in range(len(Objects))]
        
        
        for i in range(len(Objects)):
            trait = traits[i];
            if(trait == 1):
                weight += Objects[i][0];
                value += Objects[i][1];
                
                
        self.weight = weight;
        self.value = value;
        self.traits = traits;
        
    def print(self):
        print(self.value, self.weight);


def generation(population):
    
    #Remove phenotypes that are over the weight limit
    for pheno in population:
        if(pheno.weight > weightLimit):
            population.remove(pheno);

    
    #Take the best top half for this generation
    population.sort(key = lambda pheno : pheno.value, reverse = True); 
    population = population[0:len(population)//2];
    
    
    children = [];
    
    while(len(population) + len(children) < populationSize):      
        parents = random.sample(population, 2);
        
        index = random.randint(1, len(Objects) - 1);
        
        traitsA = parents[0].traits[0:index] + parents[1].traits[index:len(Objects)]      
        traitsB = parents[1].traits[0:index] + parents[0].traits[index:len(Objects)]
        
        children.append(Phenotype(traitsA));
        children.append(Phenotype(traitsB));
        
    
    population += children;
    
        
    return population;
    
    



population = [Phenotype() for i in range(populationSize)]


for i in range(2):
    population = generation(population);



for pheno in population:
    pheno.print();













        
        
            
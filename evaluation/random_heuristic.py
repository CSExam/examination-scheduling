#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
PATHS = os.getcwd().split('/')
PROJECT_PATH = ''
for p in PATHS:
    PROJECT_PATH += '%s/' % p
    if p == 'examination-scheduling':
        break
sys.path.append(PROJECT_PATH)

from time import time
from inputData import examination_data
from heuristics.MetaHeuristic import RandomHeuristic
from heuristics.schedule_times import optimize
from heuristics.johnson import Johnson
from heuristics.AC import AC

if __name__ == '__main__':
    
    threshold = 10
    gamma = 1.0
    n_colorings = 10
    epochs = 1
    annealing_iterations = 100
    
    data = examination_data.read_data(threshold = threshold)
    
    print data['n'], data['r'], data['p']
    
    #Heuristic = RandomHeuristic(data, n_colorings = n_colorings)
    Heuristic = Johnson(data, n_colorings = n_colorings, n_colors = data['p'])
    #Heuristic = AC(data, num_ants = n_colorings)
    
    t = time()
    x, y, v, logger = optimize(Heuristic, data, epochs = epochs, gamma = gamma, annealing_iterations = annealing_iterations, verbose = False, log_history = True)
    print "Time:", time()-t
    print "VALUE:", v
    
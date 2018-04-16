#!/bin/python3

import sys

def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    # pos: (population, # of clouds)
    town = {}
    for i in range(len(x)):
        town[x[i]] = {'population': p[i], 'cloud': 0}
    # print(town)
    for i in range(len(y)):
        for ri in range(-r[i], r[i] + 1):
            pos = y[i] + ri
            if pos in town:
                town[pos]['cloud'] += 1
            else:
                town[pos] = {'population': 0, 'cloud': 0}
    # print(town)
    town_with_max_population = None
    max_population = 0
    sum_population = 0
    for pos in town:
        if town[pos]['cloud'] != 1:
            if town[pos]['cloud'] == 0:
                sum_population += town[pos]['population']
            continue
        if not town_with_max_population or max_population < town[pos]['population']:
            town_with_max_population = pos
            max_population = town[pos]['population']
    if town_with_max_population is not None:
        town[town_with_max_population]['cloud'] = 0
        sum_population += town[town_with_max_population]['population']
    return sum_population

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    x = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    y = list(map(int, input().strip().split(' ')))
    r = list(map(int, input().strip().split(' ')))
    result = maximumPeople(p, x, y, r)
    print(result)

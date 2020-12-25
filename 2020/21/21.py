#!/usr/bin/python
import copy

with open('food.txt') as fh:
    lines = fh.readlines()

food = []
for line in lines:
    idx = line.index('(')
    ingredients = line[:idx]
    allergens = line[idx+1:-1]
    allergens = allergens.replace(',','')
    food.append({
        'ing': ingredients.strip().split(' '),
        'all': allergens[:-1].split(' ')[1:]
    })

ingredients = {}
allergens = {}
for meal in food:
    for ing in meal['ing']:
        ingredients[ing] = 1
    for all in meal['all']:
        allergens[all] = 1

couldBeIn = {all:copy.copy(ingredients) for all in allergens}
ingByAll = {all:copy.copy(ingredients) for all in allergens}

for allergen in ingByAll:
    for ingredient in ingByAll[allergen]:
        found = True
        for meal in food:
            if allergen in meal['all'] and ingredient not in meal['ing']:
                found = False
                break
        if not found:
            del couldBeIn[allergen][ingredient]

needpass = True
while(needpass):
    print([len(l) for l in couldBeIn.values()])
    needpass = False
    for allergen in couldBeIn:
        if len(couldBeIn[allergen]) == 1:
            ingredient = couldBeIn[allergen].keys()[0]
            for otherallergen in couldBeIn:
                if allergen != otherallergen and ingredient in couldBeIn[otherallergen]:
                    needpass = True
                    del couldBeIn[otherallergen][ingredient]

print([len(l) for l in couldBeIn.values()])
okIng = copy.deepcopy(ingredients)
for d in couldBeIn.values():
    for i in d.keys():
        print(i)
        del okIng[i]

count = 0
for meal in food:
    for ing in meal['ing']:
        if ing in okIng:
            count += 1
print(count)

final = list(couldBeIn.keys())
final.sort()
final = [couldBeIn[a].keys()[0] for a in final]
print(','.join(final))

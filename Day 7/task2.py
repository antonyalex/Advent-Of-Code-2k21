crab_positions=[int(i) for i in open("input.txt").read().split(",")]
minFuelCost = float('inf')
for i in range(max(crab_positions)):
    fuel_cost = sum([ (abs(crab - i) * (abs(crab - i) + 1) / 2) for crab in crab_positions]) 
    if fuel_cost < minFuelCost:
        minFuelCost = fuel_cost
print(minFuelCost)
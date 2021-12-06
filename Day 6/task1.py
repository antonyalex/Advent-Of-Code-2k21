fish= [int(i) for i in open("input.txt").read().split(",")]
for i in range(80):
    new_fish = []
    for i in range(len(fish)):
        if fish[i] == 0:
            new_fish.append(8)
            fish[i] = 6
        else:
            fish[i] -= 1
    fish.extend(new_fish)
print(len(fish))

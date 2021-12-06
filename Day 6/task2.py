fish=[int(i) for i in open("input.txt").read().split(",")]
days = [0]*9
for f in fish:
  days[int(f)] += 1
for d in range(256):
    next_day = [0]*9
    next_day[6] = next_day[8] = days[0]
    for d in range(8):
      next_day[d] += days[d+1]
    days = next_day

  print(sum(days))
  

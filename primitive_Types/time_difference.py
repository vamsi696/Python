time1 = 1430
time2 = 1615

t1 = (time1 // 100) * 60 + (time1 % 100)
t2 = (time2 // 100) * 60 + (time2 % 100)
difference = t2 - t1

print("Time difference:", difference, "minutes")

hours = difference // 60
print("Time difference:", hours, "hours and", difference % 60, "minutes")

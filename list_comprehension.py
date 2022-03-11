temps = [221, 123, 261, 654]

new_temps = [ temp / 10 for temp in temps]

print(new_temps)

temps2 = [221, 123, 261, -9999, 654]

new_temps2 = [ temp2 / 10 for temp2 in temps2 if temp2 != -9999]

print(new_temps2)

temps3 = [221, 123, 261, -9999, 654]

new_temps3 = [ temp3 / 10 if temp3 != -9999 else 0 for temp3 in temps3]

print(new_temps3)

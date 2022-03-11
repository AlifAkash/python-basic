monday_temperature = [ 8.1 , 9.5, 7.8, 7.3, 6.1, 6.9, 7.2]

monday_temperature.append(8.6)
print(monday_temperature)

tempIndex = monday_temperature.index(8.6)
print(tempIndex)

monday_temperature.reverse()
print(monday_temperature)

monday_temperature.clear()
print(monday_temperature)

serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]

print(serials.__getitem__(4))
print(serials[2])
print(serials[0], serials[3], serials[5])

workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print(workdays)

monday_temperature = ["Hello", 8.1 , 9.5, 7.8, 7.3, 6.1, 6.9, 7.2]

print(monday_temperature[3:5])
print(monday_temperature[:5])
print(monday_temperature[4:])
print(monday_temperature[-2])
print(monday_temperature[-7:-1])
print(monday_temperature[0])
print(monday_temperature[0][2])


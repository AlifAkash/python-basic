def celsius_to_kelvin(cels):
    return cels + 273.15

monday_temperature = [9.1, 8.8, -270.15]

for temperature in monday_temperature:
    print(celsius_to_kelvin(temperature))
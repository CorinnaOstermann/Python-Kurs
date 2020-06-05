population = {
    'Berlin': 3748148,
    'Hamburg': 1822445,
    'München': 1471508,
    'Cologne': 1085664,
    'Frankfurt': 753056
}

b = population.get("Berlin")
print(b)

for key, value in population.items():
    print(key,value)

# Beispiel Dictionary in Dictionary:
deutschland = {
    "berlin": {
    "neukölln": 3,
    "kreuzberg": 4
    }
}
print(deutschland)
deutschland["berlin"].update({"kreuzberg": 14})
print(deutschland)

# Dictionary - Einträge updaten und löschen (pop/ del):
population.update({"Berlin": 20000})
population.update({"Moskau":120000, "Dortmund": 5000})
b = population.get("Berlin")

population["Frankfurt"] = 0
berlin = population.pop("Berlin")
print("berlin:", berlin)
del population["Moskau"]

print(population)
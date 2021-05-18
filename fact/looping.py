#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
for x in range(len(farms)):
    print(farms[x])
for farm in farms:  # this will pring each item in a dictionary
    print(farm)
for farm in farms:
    print("Name: " + farm.get("name"))
    for y in range(len(farm.get("agriculture"))):
        print("  Agriculture: " + farm.get("agriculture")[y])
print()
for farm in farms:
    print("Name: " + farm.get("name"))
    for ag in farm.get("agriculture"):
        print("  Agriculture: " + ag)

print()
for farm in farms:
    x = farm.get("name")
    y = farm.get("agriculture")
    z = ",".join(y)
    print("Name: " + x + "ag" + z)

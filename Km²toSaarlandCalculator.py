print("Avaible Units: a; ha; m; km")
print("Please enter the unit")
unit = str(input())

print("How big ist the surface")

surface = int(input())
result = 0

if unit == "a":
    result = surface / 25700000
    print(result)
elif unit == "ha":
    result = surface / 257000
    print(result)
elif unit == "m":
    result = surface / 2570000000
    print(result)
elif unit == "km":
    result = surface / 2570
    print(result)

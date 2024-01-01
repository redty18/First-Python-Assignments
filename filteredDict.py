data = {
    'Alice': 30,
    'Bob': 22,
    'Charlie': 28,
    'David': 25,
}
newDict = {}

for key, value in data.items():
    if value >= 25:
        newDict[key] = value

print(newDict)
newDict = {"Name": "Adit", "Age": 20, "City": "Frisco", "Occupation": "Software Engineer"}
print(newDict)

newDict2 = {"Name": "Bob", "Hobbies": "Coding", "City": "Chandigarh", "Job": "Teacher"}

newDict["Name"] = newDict2.get("Name")
newDict["City"] = newDict2.get("City")
print(newDict)

# dictionary = {"name" : "Heb", "age" : 20, "list" : ["apple" , "banana" , "orange"], "grade" : 100, "approve" : "yes"}

# print(dictionary["list"])
# print(dictionary["name"])
# print(dictionary.keys()) = list of all keys in dictionary
# print(dictionary.values()) = list of all values in dictionary
# print(dictionary.get("approve" , "NO"))
#dictionary.items() = list of all pairs in dictionary

# personal_info = {"name" : "Adit", "age" : 20, "country" : "USA", "hobbies": ["swimming", "guitar"]}
# print(personal_info)
# print(personal_info["age"])
# personal_info["hobbies"].append("coding")
# print(personal_info["hobbies"])

dictionary2 = {}
dictionary2["Name"] = 21
dictionary2["Name2"] = 22
dictionary2["Name"] = dictionary2.get("Name", 0) + 30
dictionary2["Laptop"] = 8000
dictionary2["Laptop"] = dictionary2.get("Laptop", 0) + 13500
print(dictionary2)
print(dictionary2.get("Name3", "Incorrect"))
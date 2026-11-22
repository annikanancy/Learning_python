#Creation of dictionary
user = { 
    "name" : "Annika",
    "age" : 19,
    "skills" : ["Python", "SQL"]
}

#Accesing values
print(user["name"])
print(user.get("city", "N/A"))

user["city"] = "Sangrur"
user["age"] = 18
print(user)

#Removing items
remove_age = user.pop("age")
print(user.get("age"))

#Looping through dictionary
for key, value in user.items():
    print(f"{key}: {value}")
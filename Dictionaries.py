# ~Dictionaries~
dic = {"Arun": "Human Being",
       "Spoon": "Object"}
print(dic["Arun"]) # Accessing value using key

dic = {
    101: "Arun",
    102: "Amqn",
    103: "Shubham",
    104: "Ravi",
    105: "Tarun"
}

print(dic[101]) # Accessing value using key 
print(dic[103]) # Accessing value using key

info ={'name': "Arun Kumar",
       'age': 22, 
       'eligible': True,}
print(info)
print(info['name']) # Accessing value using key
print(info.get('name2')) # Using get() method to access value (returns None if key not found)
print(info.keys()) # Getting all keys

for key in info.keys(): # Iterating through keys
    print(info[key])

for key in info.keys(): 
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items(): # Iterating through key-value pairs
    print(f"The value corresponding to the key {key} is {value}")
    
print(info.values()) # Getting all values
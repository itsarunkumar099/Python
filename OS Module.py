# ~OS module~
import os  # Importing the os module to interact with the operating system

if (not os.path.exists("data")): # Checking if the "data" directory does not exist
    os.mkdir("data") # Creating the "data" directory
 
for i in range (0, 100): # Looping from 0 to 99
    os.mkdir(f"data/Day{i+1}") # Creating subdirectories Day1, Day2, ..., Day100 inside the "data" directory

#OR

import os  # Importing the os module to interact with the operating system
 
for i in range (0, 100): # Looping from 0 to 99
    os.rename(f"data/Day{i+1}", f"data/Tutprial {i+1}")  # Renaming subdirectories Day1, Day2, ..., Day100 to Tutorial 1, Tutorial 2, ..., Tutorial 100

#OR

import os
folders = os.listdir("data") # Listing all items in the "data" directory
print(folders) # Printing the list of items in the "data" directory

for folder in folders: # Iterating through each item in the list
    print(folder) # Printing the name of each item
    print(os.listdir(f"data/{folder}")) # Listing contents of each subdirectory

#OR

print(os.getcwd()) # Printing the current working directory

os.chdir("/Users") # Changing the current working directory to "/Users"
print(os.getcwd()) # Printing the new current working directory


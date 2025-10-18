# ~File IO~

# Reading a File
f = open('myfile 1.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

# Writing a File
f = open('myfile 1.txt', 'w')
f.write("Hello, this is a test file.")
f.close()   # Closing the file after writing

with open('myfile 1.txt','a') as f:
    f.write("\nThis line is appended to the file.")
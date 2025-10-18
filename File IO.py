# ~File IO~

# Reading a File
f = open('myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

# Writing a File
f = open('myfile.txt', 'w')
f.write("Hello, this is a test file.")
f.close()   # Closing the file after writing

with open('myfile.txt','a') as f:
    f.write("\nThis line is appended to the file.")
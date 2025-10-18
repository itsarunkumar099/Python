# ~Seek(), Tell() and Other Functions~

with open('file 1.txt', 'r') as f:
    print(type(f))          # Printing the type of file object  
    # Moce the cursor to the 10th byte in the file
    f.seek(10) 

    # Read the next 5 bytes
    print( f.tell())        # Printing the current position of the cursor   
    data = f.read(5)
    print(data)             # Printing the read data

#truncate() method
with open('file 2.txt', 'w') as f:
    f.write("Hello, this is a test file for truncate method.")
    f.truncate(20)  # Truncating the file to 20 bytes

with open('file 2.txt', 'r') as f:
    print(f.read())  # Reading the truncated file content
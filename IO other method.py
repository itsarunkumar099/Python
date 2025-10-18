# ~Read(), Readline() and other method~

# READLINE METHOD
f = open('myfile 2.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(',')[0] # extracting marks in maths
    m2 = line.split(',')[1]
    m3 = line.split(',')[2]
    print(f"marks of student {i} is maths is: {m1}")    # extracting marks in English
    print(f"marks of student {i} is English is: {m2}")
    print(f"marks of student {i} is Science is: {m3}")
    print(line)

# and

f = open('myfile 2.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(',')[0]) # converting string to integer
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])
    print(f"marks of student {i} is maths is: {m1*2}")  # multiplying marks by 2
    print(f"marks of student {i} is English is: {m2*2}")
    print(f"marks of student {i} is Science is: {m3*2}")
    print(line)

# WRITELINE METHOD
f = open('myfile 3.txt', 'w')   # Opening file in write mode
lines = ["This is line 1\n", "This is line 2\n", "This is line 3\n"]
f.writelines(lines)
f.close()

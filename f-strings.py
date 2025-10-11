# ~f-strings~
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Arun Kumar"

print(letter.format(country, name)) # str.format() way of formatting

print(f"Hey my name is {name} and I am from {country}") # f-string way of formattin

print(f"We use f-stings like this: Hey my name is {{name}} and I am from {{country}}") # To print curly braces

price = 49.099999
txt = f"For only {price:.2f} dollars!" # Formatting float to 2 decimal places
print(txt)

print(type(f"{2*30}")) # f-string can evaluate expressions
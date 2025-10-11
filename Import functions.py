# ~Import functions~

from math import sqrt, pi           # imports specific functions from math module
result = sqrt(9) * pi
print(result) # Output


from math import *                  # imports all functions from math module
result = sqrt(8) * pi
print(result) # Output

from math import pi, sqrt as s      # imports specific functions and renames sqrt to s
result = s(7) * pi
print(result) # Output

import math as m                    # imports math module and renames it to m
result = m.sqrt(6) * m.pi
print(result) # Output

import math as math_builtin_python  # imports math module and renames it to math_builtin_python
result = math_builtin_python.sqrt(5) * math_builtin_python.pi
print(result) # Output

# OR

import math
print(dir(math)) # Lists all functions and constants in the math module
print(math.nan, type(math.nan))

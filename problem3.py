# Problem of the day 3:

# Write a function that takes the variables height (h) and radius (r)
# And returns the volume of the cone

import math

def cone_volume():
    
    # Let the user enter the numbers:
    Height = float(input("Enter the Height of the cone :" ))
    Radius = float(input("Enter the Radius of the cone :" ))
    
    volume = (1/3) * math.pi *Radius**2 * Height
         
    return volume
result = cone_volume()
print(f"The volume of the cone {round(result,2)} ")
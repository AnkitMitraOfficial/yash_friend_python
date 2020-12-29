#task:
#Find area of a circle


# Basic example
"""
Radius = r = 3
Area	= π r ** 2
 	= π × 3 ** 2
 	= 3.14159... × (3 × 3)
 	= 28.2743...... 
"""
radius = int(input('Enter radius of the circle: '))
unit = int(input("Enter unit of the circle: "))

def find_area(n=radius):
    π = 3.141592654 # Default value
    result = π * n ** 2
    print(f'The area of the circle is {result}')

find_area()


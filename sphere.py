#sphere.py calculates the volume and surface area of
#a sphere based on user input 
from math import *
def sphereVolume(radius):
    volume = (radius ** 3) * pi * (4 / 3)
    return volume

def sphereArea(radius):
    area = 4 * pi * (radius ** 2)
    return area

def main():
    radius = float(input("Enter the radius length: "))
    print("The volume of the sphere is:",sphereVolume(radius))
    print("The surface area of the sphere is:",sphereArea(radius))

main()

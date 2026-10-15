#!/usr/bin/env python3
# Created By: elohim
# Date: oct 2026
# this program calculate the surface area and voulme of a cylinder
import math


def main():
    # welcome message
    print("welcome to elohim surface Area and Volume of a cylinder in progamming")
    print("")

    # get the radius and height of the cylinder form the user  and convert to float
    radius = float(input("Enter radius (cm): "))
    height = float(input("Enter height (cm): "))

    # Calculations the surface area and volume of the cylinder
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * (radius ** 2)
    volume = math.pi * (radius ** 2) * height

    # Display the surface area and volume to the user with proper unit
    print("")
    print("Surface Area is{:.2f} cm². ".format(surface_area))
    print("Volume is {:.2f} cm³.".format(volume))


if __name__ == "__main__":
    main()

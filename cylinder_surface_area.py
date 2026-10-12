#!/usr/bin/env python3

# Created By: elohim

# Date: oct, 2026


import math

# Inputs
radius = float(input("Enter radius (cm): "))
height = float(input("Enter height (cm): "))

# Calculations
surface_area = 2 * math.pi * radius * height + 2 * math.pi * (radius**2)
volume = math.pi * (radius**2) * height

# Output
print(f"Surface Area = {surface_area:.2f} cm² (exact: {surface_area:.6f})")
print(f"Volume = {volume:.1f} cm³ (exact: {volume:.6f})")


if __name__ == "__main__":
    main()

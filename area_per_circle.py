#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Sep. 21, 2022
# This program calculates the area and circumference of a circle
# with a radius of 15mm
import math


def main():
    radius = 15
    area = math.pi * (radius**2)
    circumference = 2 * (math.pi * radius)
    print(f"The area of the circle is: {area}mm^2")
    print("")
    print(f"The circumference of the circle is: {circumference}mm")


if __name__ == "__main__":
    main()

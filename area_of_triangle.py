#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This programs calculates the area of a triangle


def calculate_area(base, height):
    # calculate area

    # process & output
    if base <= 0 or height <= 0:
        print("\nInvalid Input. Try Again.")
        print("Done.")
    else:
        area = 0.5 * base * height
        print("\nThe area is {0} units²".format(area))
        print("Done.")


def main():
    # this function calls another function

    # input
    base_input = input("Enter the dimension of the base: ")
    height_input = input("Enter the dimension of the height: ")
    try:
        base = float(base_input)
        height = float(height_input)
        calculate_area(base, height)  # call function
    except(Exception):
        print("\nInvalid Input. Try Again")
        print("Done.")


if __name__ == "__main__":
    main()

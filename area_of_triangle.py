#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This programs calculates the area of a triangle


def calculate_area(base, height):
    # calculate area

    # process & output
    area = 0.5 * base * height
    print("\nThe area is {0} units²\nDone.".format(area))


def main():
    # this function receives input and calls another function

    # input
    base_input = input("Enter the dimension of the base: ")
    height_input = input("Enter the dimension of the height: ")
    try:
        base = float(base_input)
        height = float(height_input)
        if base <= 0 or height <= 0:
            print("\nInvalid Input. Try Again.\nDone.")
        else:
            calculate_area(base, height)  # call function
    except(Exception):
        print("\nInvalid Input. Try Again\nDone.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	sous_total = 0
	name = name.upper()

	for achats in data:
		sous_total += achats[1] * achats[2]

	taxes = 0.15 * sous_total

	return (f"{name} \n{'SOUS TOTAL'.ljust(10)} {sous_total:10.2f}$ \n{'TAXES'.ljust(10)} {taxes:10.2f}$ \n{'TOTAL'.ljust(10)} {sous_total + taxes:10.2f}$")


def format_number(number, num_decimal_digits):
	neg = False

	if number < 0:
		number *= -1
		neg = True

	decimal = str(int((round(number - number//1, num_decimal_digits)) * (10 ** num_decimal_digits)))
	number = str(int(number//1))
	number_spaced = number

	for i in range(len(number) - 3, 0, -3):
		number_spaced = number_spaced[:i] + " " + number_spaced[i:]

	if neg == True:
		return "-" + number_spaced + "." + decimal
	else:
		return number_spaced + "." + decimal
def get_triangle(num_rows):
	pyramid = f"{'+' * (2 * num_rows + 1)}"

	for i in range(1, num_rows + 1):
		pyramid += f"\n+{' ' * (num_rows - i)}{'A' * (i * 2 - 1)}{' ' * (num_rows - i)}+"

	return pyramid + f"\n{'+' * (2 * num_rows + 1)}"


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(123456789.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))

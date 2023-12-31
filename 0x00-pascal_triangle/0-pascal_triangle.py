#!/usr/bin/python3
"""The function creates a Pascal's triangle of n rows and returns it as a list.

:param n: The input parameter for the function pascal_triangle,
which is an integer representing the number of rows to generate
in the Pascal's triangle
:return: If n is less than or equal to 0, an empty list is being
returned. Otherwise, a list containing the numbers from 1 to n is
being returned. However, the implementation of the loop is incorrect
as it is trying to iterate over an integer value instead of a range
of values."""


def pascal_triangle(n):
    """returns a list of numbers representing the pascal triangle"""
    if n <= 0:
        return []
    else:
        # create an empty list to hold each row of the triangle
        triangle = []
        for i in range(n):
            # create a new list to hold values for each row
            tmp_list = []
            for j in range(i+1):
                # Calculate the value of each element in the row
                if j == 0 or j == i:
                    tmp_list.append(1)
                else:
                    """Each element is the sum of the two elements
                    above it in the previous row"""
                    tmp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
            # Append the row to the triangle list
            triangle.append(tmp_list)
        return triangle 
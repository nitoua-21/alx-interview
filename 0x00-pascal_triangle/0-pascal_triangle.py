#!/usr/bin/python3
"""
Pascal's Triangle
"""
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row using a recursive approach.

    Args:
    n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
    list of lists: A list containing n lists, where each inner list
    represents a row in Pascal's Triangle. Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        
        new_row.append(1)
        triangle.append(new_row)
    
    return triangle

#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (List[List[int]]): A list of list of integers where:
            - 0 represents water
            - 1 represents land

    Returns:
        int: The perimeter of the island

    Notes:
        - Each cell is square with side length of 1
        - Cells are connected horizontally/vertically only
        - Grid is completely surrounded by water
        - Grid contains only one island (or nothing)
        - The island doesn't have "lakes"
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with assuming all 4 sides contribute to perimeter
                cell_perimeter = 4

                # Check cell above
                if i > 0 and grid[i-1][j] == 1:
                    cell_perimeter -= 1
                # Check cell below
                if i < rows-1 and grid[i+1][j] == 1:
                    cell_perimeter -= 1
                # Check cell to the left
                if j > 0 and grid[i][j-1] == 1:
                    cell_perimeter -= 1
                # Check cell to the right
                if j < cols-1 and grid[i][j+1] == 1:
                    cell_perimeter -= 1

                perimeter += cell_perimeter

    return perimeter

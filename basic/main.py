grid_1 = [
    ["X", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]

grid_2 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "O", "X"]
]

grid_3 = [
    ["X", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]

grid_4 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]

def display_grid(grid):
    print(grid[0][0],"|", grid[0][1], "|", grid[0][2])
    print("--+---+--")
    print(grid[1][0], "|", grid[1][1], "|", grid[1][2])
    print("--+---+--")
    print(grid[2][0], "|", grid[2][1], "|", grid[2][2])
display_grid(grid_1)

def determine_winner(grid):
    #Goes thorough all 3 rows, and checks to see if all 3 values in a row are the same. Like X, X, X.
    for row in grid:
        if row[0] == row[1] == row[2]:
            return row[0]


# Checking the diagonal side, so we can determine who the winner is without missing any spots.
    for column in range(3):
        if grid[0][column] == grid[1][column] == grid[2][column]:
            return grid[0][column]

    if grid[0][0] == grid [1][1] == grid[2][2]:
        return grid[0][0]

    if grid[0][2] == grid [1][1] == grid[2][0]:
        return grid[0][2]

    if all(cell !=" " for row in grid for cell in row):
        return "The game is a tie"

    return None

# This is testing all four grids
for number, grid in enumerate([grid_1, grid_2, grid_3, grid_4], start=1):
    print("\nGrid",number)
    display_grid(grid)
    print("Result:", determine_winner(grid))





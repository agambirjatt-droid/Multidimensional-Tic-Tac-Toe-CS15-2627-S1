
def display_grid(grid):
    print(grid[0][0],"|", grid[0][1], "|", grid[0][2])
    print("--+---+--")
    print(grid[1][0], "|", grid[1][1], "|", grid[1][2])
    print("--+---+--")
    print(grid[2][0], "|", grid[2][1], "|", grid[2][2])


def determine_winner(grid):
    #Goes thorough all 3 rows, and checks to see if all 3 values in a row are the same. Like X, X, X.
    for row in grid:
        if row[0] == row[1] == row[2] and row [0] != " ":
            return row[0]


# Checking the diagonal side, so we can determine who the winner is without missing any spots.
    for column in range(3):
        if grid[0][column] == grid[1][column] == grid[2][column] and grid[0][column] !=" ":
            return grid[0][column]

    if grid[0][0] == grid [1][1] == grid[2][2] and grid [0][0] != " ":
        return grid[0][0]

    if grid[0][2] == grid [1][1] == grid[2][0] and grid [0][2] != " ":
        return grid[0][2]

    if all(cell !=" " for row in grid for cell in row):
        return "The game is a tie"

    return None
game_grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
display_grid(game_grid)

current_player = "X"

while True:
    print("\nPlayer", current_player)

    try:
        row = int(input("Choose one of the following rows (0-2):"))
        column = int(input("Choose one of the columns listed: "))

    except ValueError:
        print("Please enter only numbers, try again.")
        continue

    if row < 0 or row > 2 or column < 0 or column > 2:
        print(" What you just inputted is invalid. Please choose numbers from 0 to 2.")
        continue

    if game_grid [row][column] != " ":
        print("That spot has been taken by tbe other player, try again.")
        continue

    game_grid[row][column] = current_player

    display_grid(game_grid)

    result = determine_winner(game_grid)

    if result == "X" or result == "O":
        print("Player", result, "has Won!")
        break

    if result == "The game is a tie":
        print("The game is a tie!")
        break

    if current_player == "X":
        current_player = "O"

    else:
        current_player = "X"
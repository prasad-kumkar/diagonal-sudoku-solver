from utils import *

sudoku = '..3.2.6..9..3.5......8..4....81.29..7.......8..................8..2.3..9..5...3..'

grid = grid_values(sudoku)

display(search(grid))

# Futoshiki-puzzle:
My code solves a 5x5 futoshiki puzzle, given inputs of the type below. The code first reads the input file, and assigns the initial input board to hold a Piece (a python class I created) with a value initialized to the coresponding coordinate on the board. The code uses forward checking and backtracking to solve the puzzle.


Given an input file of this format:

0 0 0 0 0

0 0 0 0 0

5 0 0 0 0

0 0 0 2 0

0 0 0 0 1

-------

0 > 0 0

0 0 0 0

0 0 > 0

0 0 0 0

0 0 < 0

-------

^ ^ 0 0 0

0 0 0 0 0

0 0 0 0 0

0 v 0 0 0 

Produce an output file with a solution for the 5x5 futoshiki puzzle. Rows and columns must have all unique values.

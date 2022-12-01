# Sudoku Solver using Simulated Annealing

### By : Aditi Pradeep
### Last updated: Dec 1st, 2022

Simulated annealing is an optimization technique that uses random guesses to find solutions. This repository uses simulated annealing to solve sudokus. I enjoy solving sudokus and was just fascinated by the idea that a deterministic problem like a sudoku could be solved by simply guessing. Being a physics graduate student, the idea of taking a physical process and using it in an optimization problem seemed kind of cool.

## About the code

The overall structure of the code was inspired by the pseudocode in this page: https://en.wikipedia.org/wiki/Simulated_annealing. 

The code works as follows:

1. Uniquely fill every nxn block in an n^2^ x n^2^ puzzle randomly.
2. Count the number of unique elements in every row and column, assigning a score of -1 to each unique element.
3. Pick a random nxn square in the puzzle and swap two entries in it to calculate a "neighboring state".
4. Calculate the score for the neighbor state and accept/reject with a certain probability that the new state has a lower score.
5. Cool the temperature by some cooling rate (e.g. T= 0.99999T)
6. Repeat from step 2 till minimum score is reached.

I tried a couple of different cost functions (like various ways of scoring the number of duplicates instead), but the cost function that seemed most robust was scoring the unique elements, inspired by Erich Owen's [SudokuSolver](https://github.com/erichowens/SudokuSolver). I also found that uniquely filling blocks and scoring along the rows and columns was more robust than uniquely filling rows(columns) and scoring along the columns(rows) and blocks.

Notes:

- In principle, the code should work for a sudoku of any dimension. 
- The catch is that it has only been tested for 4x4s, 9x9s and some 16x16s. For higher dimensions, adjusting the temperatures, cooling rate and maxIterations should, in theory, solve the sudoku.
- If the puzzle isn't solved in the first attempt, retry. Since this is a random solver, the outcome is different every time. The solver was found to solve every 4x4 and 9x9 puzzle tested in the first attempt. Note that sometimes it reheats, but still solves it. I've tested at least a 100 9x9s made using the sudoku_maker module. I've only tested a few 16x16s, so the parameters for this may need fine tuning.
- If you're trying to solve your own sudoku, you need to pass it as an n^2^ x n^2^ list (e.g. 9x9) with zeros marking the empty cells.

The package has 2 modules: 
1. sudoku_maker : Contains functions to make a custom sudoku of any dimension. Note that the sudokus made using this are **not** guaranteed to have a unique solution.
2. sudoku_solver : Contains functions to solve a sudoku using simulated annealing.

## Running the solver

Required modules:
- numpy

You can install the requirements by running 

    pip install -r requirements.txt    
    
Code was developed and tested with Python 3.11.0
    
**An example jupyter notebbok has been included in Sudoku_Solver/demo that shows how to use the module and how to get documentation for various functions.**

*Contact me via email: aditipradeep314@gmail.com. Any feedback is welcome.* :-)
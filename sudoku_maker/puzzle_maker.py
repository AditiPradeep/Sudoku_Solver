import numpy as np
from random import sample, randint
from copy import deepcopy

def makeSudoku(n,verbose=False):
    '''
    Make sudoku of dimension n^2
    Input:
     n       : Dimension
     verbose : (Optional) Boolean, prints sudoku. Default value is False.

    Output:
     sudoku  : n^2 x n^2 grid of values 
     
    '''
    
    side=n*n
    
    block=sample(range(0,n),n)
    blockItr=sample(range(0,n),n)
    
    nums = sample(range(1,side+1),side)

    
    sudoku=[]
    for r in block:
        for c in blockItr:
            
            start=r+n*c
            
            gridrow=[]
            for k in range(side):
                gridrow.append(nums[(start+k)%side])
                
            sudoku.append(gridrow)

    if(verbose):
        Print(sudoku)
        
    return sudoku

#Make puzzle
def makePuzzle(grid,n,verbose=False): #n is # of elements to be removed
    '''
    Randomly remove elements from a grid to make a sudoku puzzle

    Input:
     grid    : A grid (NxN dimension) of values
     n       : Number of elements to remove.
               This determines the difficulty of the puzzle.
     verbose : (Optional) Boolean that determines whether to print results.
               Default values is False.

    Output:
     puzzle  : a sudoke puzzle with zeros indicating the empty cells
    '''
    
    temp_grid = deepcopy(grid)
    side = len(grid)
    if(n>=side*side):
        raise ValueError(f"Cannot remove {n} elements from grid with {side*side} elements!")
    
    indices = np.random.choice(range(side*side),n,replace=False)
    
    for i in range(n):
        rows = indices[i]//side
        cols = indices[i]%side
        temp_grid[rows][cols] = 0
    
    if(verbose):
        Print(temp_grid)
        
    return temp_grid

    
def getBlockIndices(start, dim):
    '''
    Get the list indices for a block
    '''
    return list(range(start,start+dim))

def checkValidSudoku(puzzle):
    '''
    Check if a filled grid is valid, i.e. follows all sudoku rules

    Input:
     puzzle : The grid to be checked

    Output:
     Returns boolean status of the puzzle
    '''

    
    side = len(puzzle)
    dim = int(np.sqrt(side))
    
    sqr=0
    sqc=0
    for r in range(side):
        row = np.array(puzzle[r])
        column = np.array(puzzle)[:,[r]].transpose()[0]
        
        ri = getBlockIndices(sqr,dim)
        ci = getBlockIndices(sqc,dim)
        square = np.array(puzzle)[ri,:][:,ci].reshape(side)
        
        sqr=sqr+dim
        
        if(sqr == side):
            sqr = 0
            sqc = sqc + dim
            
        for val in range(1,side+1):
            if(len(np.where(row==val)[0])>1 or len(np.where(column==val)[0])>1 or len(np.where(square==val)[0])>1):
                return False
            
    return True


#Print grid
def Print(puzzle):
    '''
    Print a grid

    Input:
     puzzle: The grid to be printed

    Output:
     Returns nothing, but prints the puzzle
    '''
    side=len(puzzle)
    n= int(np.sqrt(side))
    

    factor=2*(n+1)+ (side-n) + (2*2*side+side)
    
    print('-'*factor)
    for i in range(side): 
        temp=''
        for j in range(side):
            
            #For single digits
            if(len(str(puzzle[i][j]))==1):
                if(j!= side-1):
                    if(j%n==0):
                        temp+='||  '+str(puzzle[i][j])+'  |  '
                    elif(j%n == n-1):
                        temp+=str(puzzle[i][j])+'  '
                    else:
                        temp+=str(puzzle[i][j])+'  |  '
                    
                else:
                    temp+= str(puzzle[i][j]) + '  ||'
            
            #For double digits
            else:
                if(j!= side-1):
                    if(j%n==0):
                        temp+='|| '+str(puzzle[i][j])+'  |  '
                    elif(j%n == n-1):
                        temp+=str(puzzle[i][j])+' '
                    else:
                        temp+=str(puzzle[i][j])+' |  '
                    
                else:
                    temp+= str(puzzle[i][j]) + ' ||'
               
                
        print(temp)
        
        if(i%n ==n-1):
            line = '-'*factor
            print(line)
    
    return


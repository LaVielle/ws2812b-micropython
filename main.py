from enum import Enum
import math

class Button(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

numColumns = 2
columnMin = 0 # the index of the left most column
columnMax = numColumns-1 # the index of the right most column

numRows = 2
rowMin = 0 # the index of the top row
rowMax = numRows-1 # the index of the bottom row

activeCellIndex = 0

# Cell class
class Cell:
  def __init__(self, row, column):
    self.row = row
    self.column = column
    self.active = False
  def __str__(self):
        return "{row: %s, column: %s, active: %s}" % (self.row, self.column, self.active)

# List that will hold all our Cell instances
grid = []

indexFromCoordsMap = {}

def getIndexFromCoords(row,column):
    return row * numColumns + column
    
def getCoordsFromIndex(index):
    row = math.floor(index / numColumns)
    column = index - row * numColumns
    return ({"row": row, "column": column})
    
print(getCoordsFromIndex(0))
print(getCoordsFromIndex(1))
print(getCoordsFromIndex(2))
print(getCoordsFromIndex(3))
 
# generateGrid: Populates the grid list with Cell instances
def generateGrid():
    for rowIndex in range(numRows):
        for columnIndex in range(numColumns):
            cell = Cell(rowIndex, columnIndex)
            indexFromCoordsMap[f'{cell.row},{cell.column}'] = len(grid)
            grid.append(cell)
        
# A utility to print the grid list content
def printGrid():  
    print("--- Grid ---")
    for i in grid:
        print(i)
    print("")
    

def initActiveCell():
    grid[activeCellIndex].active = True
  
# Turns off previous active cell (aka current active cell) and turns on next active cell (aka new active cell)
def updateActiveCell(currentActiveCellIndex, newActiveCellIndex):
    grid[currentActiveCellIndex].active = False
    grid[newActiveCellIndex].active = True

# Handler for various button presses
def onButtonPress(button):
    if (button == Button.UP):
        print('UP!')
        
        # variable that holds current active cell data
        activeCell = grid[activeCellIndex]
        
        # variable that will be used to calculate next row position
        targetRow = activeCell.row
        
        if (activeCell.row == rowMin):
            # current active cell is on top row => move to bottom row
            targetRow = rowMax
        else:
            # move to row above current row
            targetRow -= 1
            
        newActiveCellIndex = getIndexFromCoords(targetRow, activeCell.column)
        updateActiveCell(activeCellIndex, newActiveCellIndex)
        
        
    else:
        print('other button')
    
   
# Generate grid and turn on initial active cell
generateGrid()
initActiveCell()
printGrid()

# Press UP button
onButtonPress(Button.UP)

printGrid()
print(activeCellIndex)
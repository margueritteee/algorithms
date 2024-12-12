#kezrane margueritte IAA (sudoku solver code using backtracking)
#how sudoku works ? we verify each time if the number exists in (row-column-box) if not we add it , if yes we use backtracking and go back to re-verify (using backtracking)
#complexity in the worst case (we try in each cell the numbers from 1 to 9 and we try all the cells 9x9=81) so its O(9^81)


#0 means its empty
example=[
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


#we need to have a validation function that checks if a certain try is valid or no
def is_valid_action(example,row,col,number):
    for x in range(9):
        if example[row][x]==number:
            return False   #if in the same row we have this exact number this cant be valid action
    for x in range(9):
        if example[x][col]==number:
            return False   #if in the same column we have this exact number this cant be valid action
    corner_row = row-row %3 #we find top left row of the 3x3 box
    corner_column = col-col %3 
    #if in the same box
    for x in range(3): #row
        for y in range(3): #column
            if example[corner_row+x][corner_column+y]==number:
                return False
    return True        

#backtracking function (the solver one)
def solve(example,row,col):
    if col==9: #overbaord the columns (we start from 0 to 8)
        if row==8: #last row
            return True #we have the solution , weve reached the final point
        row +=1 #we go to a new row
        col=0 #and we start from the first column again
    if example[row][col]>0 : #if we already have a value
        return solve(example,row,col + 1) #we pass to the next value
    for number in range(1,10): #1,2,3,...,9
        if is_valid_action(example,row,col,number):
            example[row][col]=number #if its valid we assume its the correct solution
            #if we r at the end of the example we return true cause its solved (recursive ladder)
            if solve(example,row,col+1):
                return True
        example[row][col]=0 #if its not valid we leave it at zero (backtracking)
    return False #it means there is no possible solution 



if solve(example,0,0):
    for i in range(9):
        for j in range(9):
            print (example[i][j], end=" ")
        print()
else:
    print("no solution available")


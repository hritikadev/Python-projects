Board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],                #0,0     0,1     0,2
    [0,0,0,6,0,1,0,7,8],                #1,0     1,1     1,2
    [0,0,7,0,4,0,2,6,0],                #2,0     2,1     2,2
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def PrintBoard(board):
    for i in range(len(board)):
        if i%3 == 0 and i !=0:
            print("------------------------")
        for j in range(len(board[0])):
            if j%3 == 0 and j !=0:
                print(" | ", end="")
            if j != 8:
                print(str(board[i][j]) + " ", end = "")
            else:
                print(board[i][j])
#find the next empty space denoted by 0
def EmptySpace(board): 
    for i in range(len(board)):  #gives no. of rows
        for j in range(len(board[0])): #no, of cols in the row
            if board[i][j] == 0:
                return (i, j)  #row,col
    return None

def ValidInput(board, num, pos):
    for i in range(len(board[0])):      #for rows
        if board[pos[0]][i] == num and pos[1] !=i:
            return False

    for i in range(len(board)):         #fro cols
        if board[i][pos[1]] == num and pos[0] !=i:
            return False

    box_x = pos[1] //3
    box_y = pos[0] //3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and pos != (i,j):
                return False
    return True

def SolveSudoko(board):
    print(board)
    next_space = EmptySpace(board)
    if not next_space:
        return True
    else:
        row, col = next_space
    for i in range(1, 10):
        if ValidInput(board, i, (row, col)):
            board[row][col] = i

            if SolveSudoko(board):
                return True
            board[row][col] = 0
    return False
            
PrintBoard(Board)
SolveSudoko(Board)
print("******************")
PrintBoard(Board)


    
import random

solvedBoard = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
posOfZero = (3,3)

def movePiece(piece: int) -> bool:
    global board
    global posOfZero
    
    possibleMoves = getPossibleMoves()
    
    for move in possibleMoves:
        if move[0] == piece:
            board[move[1][0]][move[1][1]] = 0
            board[posOfZero[0]][posOfZero[1]] = move[0]
            posOfZero = move[1]

            return True
    else:
        return False

def getPossibleMoves() -> list:
        moves = []
        if posOfZero[0] != 3:
            moves.append((board[posOfZero[0]+1][posOfZero[1]], (posOfZero[0]+1,posOfZero[1])))
        if posOfZero[1] != 3:
            moves.append((board[posOfZero[0]][posOfZero[1]+1], (posOfZero[0],posOfZero[1]+1)))
        if posOfZero[0] != 0:
            moves.append((board[posOfZero[0]-1][posOfZero[1]], (posOfZero[0]-1,posOfZero[1])))
        if posOfZero[1] != 0:
            moves.append((board[posOfZero[0]][posOfZero[1]-1], (posOfZero[0],posOfZero[1]-1)))
        return moves

def printBoard() -> None:
    for row in board:
        for num in row:
            if num == 0:
                print(end="    ")
            else:
                if len(str(num)) == 1:
                    print(end=f"0{num}  ")
                else:
                    print(end=f"{num}  ")
        print()

def scramble():
    for _ in range(200): 
        moves = getPossibleMoves()
        move = random.choices(getPossibleMoves())[0][0]
        movePiece(move)

if __name__ == "__main__":
    scramble()
    while True:
        print()
        printBoard()
        move = input("\nmove--> ").removeprefix("0")

        if not movePiece(int(move)):
            print("move not possible")
        elif board == solvedBoard:
            printBoard()
            print("\nsolved :)")
            exit()

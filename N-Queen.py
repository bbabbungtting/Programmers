#x,y 좌표, 크기 N, 체크판 board
def findRoute(x,y,N,board):
    for i in range(N):
        board[i][y]=1

    for j in range(N):
        board[x][j]=1
    
    min_n = min(x,y)

    i = x - min_n
    j = y - min_n

    while(i<N and j<N):
        board[i][j] = 1
        i += 1
        j += 1


#판출력
def printBoard(N,board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=' ')
        print(' ')


N = 4
answer = 0

board = [[0 for j in range(N)] for i in range(N)]

for n in range(N):
    for x1 in range(n,N):
        for y1 in range(N):
            #첫번째 퀸 배치
            findRoute(x1,y1,N,board)

            for x2 in range(N):
                for y2 in range(N):
                    if(board[x2][y2]==0):
                        findRoute(x2,y2,N,board)
                    
                    #...

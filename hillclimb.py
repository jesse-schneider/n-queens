import random
from queens_board import QueensBoard

def hillclimb(QueensBoard):
    #step 1: initalise random board with all N Queens on the board
    for queen in QueensBoard.queens:
            col = random.randint(0, QueensBoard.n-1)
            row = random.randint(0, QueensBoard.n-1)
            #if value is already a queen
            if QueensBoard.queens[row][col] == 1:
                #re-randomise the col and row values
                col = random.randint(0, QueensBoard.n-1)
                row = random.randint(0, QueensBoard.n-1)
            QueensBoard.queens[row][col] = 1
            xy = [row, col]
            QueensBoard.positions.append(xy)
        QueensBoard.print_board()
        print(QueensBoard.positions)
        #step 2: calculate the error cost of the random board
        cost = QueensBoard.cost_function()
        print("cost: ", cost)
        QueensBoard.find_neighbors()
        #step 3: find some neighbors close to this solution (move queens)
        #step 4: evaluate neighbors - if cost is closer to zero, move to that board
        #cost function - try to get to zero
        # value of cost == number of queens that are attacking each other - try to get to zero

def cost_function(QueensBoard):
    cost = 0
     #calculate the number of times queens are colliding with each other
    for i in range(QueensBoard.n):
        for j in range(i+ 1, QueensBoard.n):
            #check if queens in same row
            if QueensBoard.positions[i][0] == QueensBoard.positions[j][0]:
                    cost += 1
                #check if queens in same column
                if QueensBoard.positions[i][1] == QueensBoard.positions[j][1]:
                    cost += 1
                #check diagonals
                x_dist = abs(QueensBoard.positions[i][0] - QueensBoard.positions[j][0])
                y_dist = abs(QueensBoard.positions[i][1] - QueensBoard.positions[j][1])
                # gradient = rise / run - if gradient == 1, then queens are on same diagonal
                if x_dist == 0:
                    #avoid division by zero - if zero, then definitely not on diagonals
                    continue
                gradient = y_dist / x_dist
                if(abs(gradient) == 1):
                    cost += 1                         
        return cost

    def find_neighbors(QueensBoard):
        #function to find a similar solution to the previous solution
        # new_positions = []
        for i in range(QueensBoard.n):
            xy = QueensBoard.positions[i]
            if xy[0] < QueensBoard.n:
                xy[0] += 1
            elif xy[0] > 0:
                xy[0] -= 1
            if
            xy[1] += 1 
            QueensBoard.positions[i] = xy
        print(QueensBoard.positions)
        print(QueensBoard.cost_function())
        return

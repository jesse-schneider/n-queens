from queue import Queue
import copy
import time
import random

class QueensBoard:
    def __init__(self, n,  row=0, queens=[], x_coordinate=[]):
        self.n = n
        self.queens = queens
        self.row = row
        self.x_coordinate = x_coordinate
        self.positions = []

    def create_board(self):
        self.queens = [[0 for i in range(self.n)] for j in range(self.n)]
        self.x_coordinate = [0 for i in range(self.n)]
    

    def print_board(self):
        for i in range(len(self.queens)):
            print(self.queens[i])
        print()

    def bfs_check_collisons(self):
    #for every queen on the board, check against every other queen
        for i in range(self.n):
            for j in range(i + 1, self.n):
                #check if queens are clashing
                if(self.x_coordinate[i] == self.x_coordinate[j]):
                    return False
                else:
                    #check diagonals
                    x_dist = abs(self.x_coordinate[i] - self.x_coordinate[j])
                    y_dist = abs(i - j)
                    #gradient = rise / run - if gradient == 1, then queens are on same diagonal
                    gradient = y_dist / x_dist
                    if(abs(gradient) == 1):
                        return False
        return True
    
    def breadth_first_search(self):
        number_solutions = 0
        #1 value to denote a queen placed on a board of 0's
        queen = 1
        #positions object to store all visited boards
        explored = {
            str(self.queens): True,
        }

        #create Queue data structure for BFS and add initial board to the queue
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            #get the next state in the queue, get it's individual values to manipulate
            current_state = queue.get()
            current_queens = current_state.queens
            current_row = current_state.row
            current_coords = current_state.x_coordinate

            for i in range(self.n):
                if current_row >= self.n:
                    continue
                # copy the current board and placed queen coordinates into new data structures
                new_queens = copy.deepcopy(current_queens)
                new_coords = copy.deepcopy(current_coords)

                # place the new queen on the new board
                new_queens[current_row][i] = queen
                new_coords[current_row] = i

                # if this board has already been explored, then do not add back into queue
                if str(new_queens) in explored:
                    continue

                #create a new state to go in the queue, add 1 to the row to increment for next time
                new_state = QueensBoard(self.n,  current_row + 1, new_queens, new_coords)

                if (current_row + 1) == self.n:
                    #check goal state
                    result = new_state.bfs_check_collisons()
                    if result and self.n <= 6:
                        print("new goal state!")
                        number_solutions += 1
                        new_state.print_board()
                    elif result:
                        print("new goal state!")
                        number_solutions += 1
                #add this new board into the queue
                queue.put(new_state)

                #record the current board in the 'explored' positions - make sure not to explore it again
                explored[str(new_queens)] = True
        return number_solutions
    


    def hillclimb(self):
        #step 1: initalise random board with all N Queens on the board
        for queen in self.queens:
            col = random.randint(0, self.n-1)
            row = random.randint(0, self.n-1)
            #if value is already a queen
            if self.queens[row][col] == 1:
                #re-randomise the col and row values
                col = random.randint(0, self.n-1)
                row = random.randint(0, self.n-1)
            self.queens[row][col] = 1
            xy = [row, col]
            self.positions.append(xy)
        self.print_board()
        print(self.positions)
        #step 2: calculate the error cost of the random board
        cost = self.cost_function()
        print("cost: ", cost)
        self.find_neighbors()
        #step 3: find some neighbors close to this solution (move queens)
        #step 4: evaluate neighbors - if cost is closer to zero, move to that board
        #cost function - try to get to zero
        # value of cost == number of queens that are attacking each other - try to get to zero
    
    def cost_function(self):
        cost = 0
        #calculate the number of times queens are colliding with each other
        for i in range(self.n):
            for j in range(i+ 1, self.n):
                #check if queens in same row
                if self.positions[i][0] == self.positions[j][0]:
                    cost += 1
                #check if queens in same column
                if self.positions[i][1] == self.positions[j][1]:
                    cost += 1
                #check diagonals
                x_dist = abs(self.positions[i][0] - self.positions[j][0])
                y_dist = abs(self.positions[i][1] - self.positions[j][1])
                # gradient = rise / run - if gradient == 1, then queens are on same diagonal
                if x_dist == 0:
                    #avoid division by zero - if zero, then definitely not on diagonals
                    continue
                gradient = y_dist / x_dist
                if(abs(gradient) == 1):
                    cost += 1                         
        return cost

    def find_neighbors(self):
        #function to find a similar solution to the previous solution
        # new_positions = []
        for i in range(self.n):
            xy = self.positions[i]
            if xy[0] < self.n:
                xy[0] += 1
            elif xy[0] > 0:
                xy[0] -= 1
            if
            xy[1] += 1 
            self.positions[i] = xy
        print(self.positions)
        print(self.cost_function())
        return 




board = QueensBoard(4)
board.create_board()
start_time = time.time()
# solutions = board.breadth_first_search()
board.hillclimb()
print("time taken: %s" % (time.time() - start_time), " seconds")
# print("number of solutions: ", solutions)

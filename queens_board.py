from queue import Queue
import copy
import time

class QueensBoard:

    def __init__(self, n,  row=0, queens=[], x_coordinate=[]):
        self.n = n
        self.queens = queens
        self.row = row
        self.x_coordinate = x_coordinate

    def create_board(self):
        self.queens = [[0 for i in range(self.n)] for j in range(self.n)]
        self.x_coordinate = [0 for i in range(self.n)]
    

    def print_board(self):
        for i in range(len(self.queens)):
            print(self.queens[i])
        print()

    def check_n_queens(self):
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
        #dict object to store all visited boards
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
                    result = new_state.check_n_queens()
                    
                    
                    if result and self.n <= 6:
                        print("new goal state!")
                        number_solutions += 1
                        new_state.print_board()
                    elif result:
                        print("new goal state!")
                        number_solutions += 1
                #add this new board into the queue
                queue.put(new_state)

                #record the current board in the 'explored' dict - make sure not to explore it again
                explored[str(new_queens)] = True
        return number_solutions


board = QueensBoard(1)
board.create_board()
start_time = time.time()
solutions = board.breadth_first_search()
print("time taken: %s" % (time.time() - start_time), " seconds")
print("number of solutions: ", solutions)

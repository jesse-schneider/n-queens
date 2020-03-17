from queue import Queue
import copy
import time
from queens_board import QueensBoard

def breadth_first_search(Board):
    number_solutions = 0
    # value to denote a queen placed on a board of 0's
    queen = 1

    #positions object to store all visited boards
    explored = {
        str(Board.queens): True,
    }

    #create Queue data structure for BFS and add initial board to the queue
    queue = Queue()
    queue.put(Board)

    while not queue.empty():
        #get the next state in the queue, get it's individual values to manipulate
        current_state = queue.get()
        current_queens = current_state.queens
        current_row = current_state.row
        current_coords = current_state.x_coordinate

        for i in range(Board.n):
            if current_row >= Board.n:
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
            new_state = QueensBoard(Board.n,  current_row + 1, new_queens, new_coords)

            if (current_row + 1) == Board.n:
                #check goal state
                result = new_state.bfs_check_collisons()
                if result and Board.n <= 6:
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

board = QueensBoard(6)
board.create_board()
start_time = time.time()
solutions = breadth_first_search(board)
print("time taken: %s" % (time.time() - start_time), " seconds")
print("number of solutions: ", solutions)


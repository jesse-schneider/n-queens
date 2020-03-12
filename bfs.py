from queue import Queue
import copy

#function to create a new N-Queens board of N x N size
def create_new_n_board(n):
    queens = [[0 for i in range(n)] for j in range(n)]
    begin = {
        "queens": queens,
        "row": 0,
        "solutions": 0,
        "x_coordinate": [0, 0, 0, 0],
    }
    return begin

#function to print the N-Queens Board
def print_board(board):
    for i in range(len(board)):
            print(board[i])
    print()

#function to check if board == goal state
def check_n_queens(state):
    num = state["row"]
    q_coords = state["x_coordinate"]

    #for every queen on the board, check against every other queen
    for i in range(num):
        for j in range(i + 1, num):
            #check if queens are clashing
            if(q_coords[i] == q_coords[j]):
                return False
            else:
            #check diagonals
                x_dist = abs(q_coords[i] - q_coords[j])
                y_dist = abs(i - j)
                #gradient = rise / run - if gradient == 1, then queens are on same diagonal
                gradient = y_dist / x_dist
                if(abs(gradient) == 1):
                    return False
    return True


def breadth_first_search(board, n):
    #1 value to denote a queen placed on a board of 0's
    queen = 1
    #dict object to store all visited boards
    explored = {
    str(board["queens"]): True,
    }

    #create Queue data structure for BFS
    queue = Queue()

    #add initial board to the queue
    queue.put(board)

    while not queue.empty():
        #get the next state in the queue, get it's individual values to manipulate
        current_state = queue.get()
        current_queens = current_state["queens"]
        current_row = current_state["row"]
        current_coords = current_state["x_coordinate"]
        
        for i in range(n):
            if current_row >= n:
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
        
            # print_board(new_queens)

            #create a new state to go in the queue, add 1 to the row to increment for next time
            new_state = {
                "queens": new_queens,
                "row": current_row + 1,
                "solutions": 0,
                "x_coordinate": new_coords,
            }

            if (current_row + 1) == n:
                #check goal state
                if check_n_queens(new_state):
                    print("goal state!")
                    print_board(new_state["queens"])

            #add this new board into the queue
            queue.put(new_state)

            #record the current board in the 'explored' dict - make sure not to explore it again
            explored[str(new_queens)] = True

begin = create_new_n_board(4)

breadth_first_search(begin, 4)


from queue import Queue
import copy

#function to create a new N-Queens board of N x N size
def create_new_n_board(n):
    queens = [[0 for i in range(n)] for j in range(n)]
    begin = {
        "queens": queens,
        "row": 0,
        "solutions": 0,
        "q_coordinates": [],
        "number_queens": 0
    }
    return begin

#function to print the N-Queens Board
def print_board(board):
    for i in range(len(board)):
            print(board[i])
    print()

#function to check if board == goal state
def check_n_queens(state):
    num = state["number_queens"]
    q_coords = state["q_coordinates"]
    print("coords: ", state["q_coordinates"])

    for i in range(num):
        for j in range(i, num):
            print("first coord: ", q_coords[i], " second coord: ", q_coords[j])
            #check if x, y clashes with any other pairs
            if(q_coords[i][0] == q_coords[j][0]):
                return False
            if (q_coords[i][1] == q_coords[j][1]):
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
        current_coords = current_state["q_coordinates"]
        current_number_queens = current_state["number_queens"]
        
        for i in range(n):
            if current_row >= n:
                continue
            #copy the current state, into a new board
            new_queens = copy.deepcopy(current_queens)

            #place the new queen on the new board
            new_queens[current_row][i] = queen
            new_queen_coords = (current_row, i)
            print("new coords: ", new_queen_coords)
            print("current coords: ", current_coords)
            new_number_queens = current_number_queens + 1
            
            #if this board has already been explored, then do not add back into queue
            if str(new_queens) in explored:
                continue

            # current_coords[current_row] = new_queen_coords
        
           
            # print_board(new_queens)

            #create a new state to go in the queue, add 1 to the row to increment for next time
            new_state = {
                "queens": new_queens,
                "row": current_row + 1,
                "solutions": 0,
                "q_coordinates": current_coords,
                "number_queens": new_number_queens,
            }

            if new_number_queens == n:
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


#i need to work out how to save a board's queens coords correctly for each state without overwriting
# then fix the find goal state function


from queue import Queue
import copy

def create_new_n_board(n):
    queens = [[0 for i in range(n)] for j in range(n)]
    begin = {
        "queens": queens,
        "row": 0,
        "solutions": 0,
    }
    return begin

def print_board(board):
    for i in range(len(board)):
            print(board[i])
    print()

queen = 1
num = 3

queue = Queue()

begin = create_new_n_board(num)

explored = {
    str(begin["queens"]): True
}

queue.put(begin)

while not queue.empty():
    #get the next state in the queue
    current_state = queue.get()
    current_queens = current_state["queens"]
    current_row = current_state["row"]
    print_board(current_queens)
    
    for i in range(num):
        if current_row >= num:
            continue
        #copy the current state, into a new board
        new_queens = copy.deepcopy(current_queens)

        #place the new queen on the new board
        new_queens[current_row][i] = queen
        
        #if this board has already been explored, then do not add back into queue
        if str(new_queens) in explored:
            continue

        #create a new state to go in the queue, add 1 to the row to increment for next time
        new_state = {
            "queens": new_queens,
            "row": current_row + 1,
            "solutions": 0,
        }

        #add this new board into the queue
        queue.put(new_state)
        #record the current board in the 'explored' dict - make sure not to explore it again
        explored[str(new_queens)] = True

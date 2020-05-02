import copy
import time
from queens_board import QueensBoard

def hillclimb(QueensBoard, cost):
    # while the board is not solved
    while (cost > 0):
        # get set of configurations within 1 move of current board
        boards = find_neighbors(QueensBoard)
        temp_cost = cost
        # for each neighbor board, check if cost is better
        for i in range(len(boards)):
            new_cost = boards[i].cost
            # if cost is better, swap boards
            if new_cost < cost:
                #switch current board with the new one
                QueensBoard = boards[i]
                cost = QueensBoard.cost
        # if cost didn't change -> local max found, exit and restart the board
        if temp_cost == cost:
            return cost
    if (cost == 0):
        # solution has been found
        print("solution found:")
        QueensBoard.print_board()
    return cost


def find_neighbors(Board):
    #find all boards with a queen moved one "move" (either up or down)
    new_boards = []
    for i in range(Board.n):
        # move ith queen up one space, add board to neighbors list
        if Board.positions[i][0] == 0:
            # cannot move up
            continue
        else:
            # perform a single move up for ith queen
            new_board = copy.deepcopy(Board)
            new_board.queens[new_board.positions[i][0]][new_board.positions[i][1]] = 0
            new_board.positions[i][0] -= 1
            new_board.queens[new_board.positions[i][0]][new_board.positions[i][1]] = 1
            new_board.cost = new_board.cost_function()
            new_boards.append(new_board)
    
    for i in range(Board.n):
        # move ith queen down one space, add board to neighbors list
        if Board.positions[i][0] == (Board.n - 1):
            # cannot move down
            continue
        else:
            # perform a single move down for ith queen
            new_board = copy.deepcopy(Board)
            new_board.queens[new_board.positions[i][0]][new_board.positions[i][1]] = 0
            new_board.positions[i][0] += 1
            new_board.queens[new_board.positions[i][0]][new_board.positions[i][1]] = 1
            new_board.cost = new_board.cost_function()
            new_boards.append(new_board)
    return new_boards


cost = 1
first = True
start_time = time.time()
while (cost > 0):
    board = QueensBoard(6)
    board.create_local_board()
    cost = board.cost_function()
    if first:
        print("\nInitial board: ")
        board.print_board()
        first = False
    cost = hillclimb(board, cost)
print("time taken: %s" % (time.time() - start_time), " seconds")
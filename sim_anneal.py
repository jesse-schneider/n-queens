import random
import copy
import time
import math
from queens_board import QueensBoard
import matplotlib.pyplot as plt

def sim_anneal(QueensBoard, T, alpha):
    print("\nInitial board: ")
    QueensBoard.print_board()
    print('cost = {}'.format(QueensBoard.cost_function()))
    K = QueensBoard.n
   
    cost = QueensBoard.cost_function()
    costs = []
    while (T > 0):
        # while the board is not solved
        for k in range(K):
            costs.append(cost)
            # get set of configurations within 1 move of current board
            board = find_neighbor(QueensBoard)
            if board == False:
                continue
            new_cost = board.cost_function()
            
            # solution has been found
            if (cost == 0):
                print("solution found:")
                QueensBoard.print_board()
                print('cost = {}'.format(QueensBoard.cost_function()))
                return costs
            elif new_cost < cost:
                #switch current board with the new one
                QueensBoard = board
                cost = new_cost
            else:
                #no good neighbor, simulate annealing
                delta = cost - new_cost
                p = math.exp((delta / T))
                prob = random.random()
                if prob < p:
                    QueensBoard = board
                    cost = new_cost
        T = alpha * T    

def find_neighbor(Board):
    #find all boards with a queen moved one "move" (either up or down)
    new_board = copy.deepcopy(Board)
    queen_to_move = random.randint(0, Board.n - 1)
    new_board.queens = [[0 for i in range(new_board.n)] for j in range(new_board.n)]

    new_board.positions[queen_to_move][0] = random.randint(0, Board.n - 1)
    if is_valid_move(new_board.positions[queen_to_move][0], new_board.n):
        for i in range(len(new_board.positions)):
            new_board.queens[new_board.positions[i][0]][new_board.positions[i][1]] = 1
        return new_board
    else:
        return False

def is_valid_move(new_val, n):
    return 0 <= new_val < n

alpha = 0.9
T = 0.3



board = QueensBoard(10)
board.create_local_board()

start_time = time.time()
graph = sim_anneal(board, T, alpha)
print("time taken: %s" % (time.time() - start_time), " seconds")
plt.plot(graph)
plt.ylabel('Cost')
plt.show()
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
        self.cost = 0

    def create_board(self):
        self.queens = [[0 for i in range(self.n)] for j in range(self.n)]
        self.x_coordinate = [0 for i in range(self.n)]

    def create_local_board(self):
        #step 1: initalise random board with all N Queens on the board
        self.queens = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            col = i
            row = random.randint(0, self.n-1)
            self.queens[row][col] = 1
            xy = [row, col]
            self.positions.append(xy)
    

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
    
    
    def cost_function(self):
        cost = 0
        #calculate the number of times queens are colliding with each other
        for i in range(self.n):
            for j in range(i+ 1, self.n):
                #check if queens in same row
                if self.positions[i][0] == self.positions[j][0]:
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
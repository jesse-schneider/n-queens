from queue import Queue
import copy

#values for moving left, right, down, up and right
# x-axis = [-1, 1, 0, 0 ]
# y-axis = [0, 0, -1, 1]

queen = 1
n = 0

queue = Queue()


begin = {
    "queens" : [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ],
}


queue.put(begin)

while queue.not_empty():
    #get the next state in the queue
    current_state = queue.get()
    current_queens = current_state["queens"]


    for i in range(3):
        new_queens = copy.deepcopy(current_queens)
        new_queens[i][n] = 1


        new_state = {
            "queens": new_queens,
        }

        q.put(new_state)

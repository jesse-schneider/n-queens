import numpy as np
import math
import matplotlib.pyplot as plt

# Parameters
K = 10000

# Initial temperature
T = 0.02

# Decay factor of the temperature
alpha = 0.9999

# Constant
max_loops = 5
inf = 1000000007
dx = np.array([-1, 1, 0, 0])
dy = np.array([0, 0, -1, 1])
direction = ['UP', 'DOWN', 'LEFT', 'RIGHT']
goal_config = np.array([
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
])


def is_valid(x, y):
    return 0 <= x <= 2 and 0 <= y <= 2


def evaluate(config):
    res = 0
    for i in range(1, 9):
        x, y = np.where(config == i)
        goal_x, goal_y = np.where(goal_config == i)
        res += abs(x[0] - goal_x[0]) + abs(y[0] - goal_y[0])

    return 1. / (res + 1)


flat_list = np.array([9, 1, 2, 3, 4, 5, 6, 7, 8])  # 9: empty cell
permutation = np.random.permutation(9)
# current_config = flat_list[permutation].reshape((3, 3))
current_config = np.array([[6, 1, 3], [2, 4, 5], [9, 8, 7]])

current_x, current_y = np.where(current_config == 9)
current_x, current_y = current_x[0], current_y[0]

print('Start config:')
print(current_config)

loops = 0
finished = False
objective_values = []
while loops < max_loops:
    loops += 1
    if finished:
        break

    for k in range(K):
        current_value = evaluate(current_config)
        objective_values.append(current_value)

        print('k = {}, E = {}'.format(k, current_value))

        if current_value == 1.:
            print('Reach goal configuration')
            print(current_config)
            finished = True
            break

        i_random = np.random.randint(0, 4)
        next_x = current_x + dx[i_random]
        next_y = current_y + dy[i_random]

        if is_valid(next_x, next_y):
            next_config = current_config.copy()
            next_config[current_x, current_y] = current_config[next_x, next_y]
            next_config[next_x, next_y] = 9

            next_value = evaluate(next_config)

            if next_value >= current_value:
                # print(direction[i_random])
                current_value = next_value
                current_config = next_config.copy()
                current_x = next_x
                current_y = next_y
            else:
                p = math.exp(-(current_value - next_value) / T)
                # print('T = {}'.format(T))
                # print(-(current_value - next_value) / T)
                print('p = {}'.format(p))
                head = np.random.choice(2, 1, replace=False, p=[1 - p, p])
                if head == 1:
                    # print(direction[i_random])
                    current_value = next_value
                    current_config = next_config.copy()
                    current_x = next_x
                    current_y = next_y

    T = alpha * T

plt.plot(objective_values)
plt.ylabel('Objective Values')
plt.show()

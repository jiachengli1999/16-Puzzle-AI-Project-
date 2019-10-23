# 14-puzzle problem
# 4x4 grid
import math
from copy import copy, deepcopy

class Node:
    def __init__(self, state, parent, action, depth, path_cost, manhatten_dist):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.children = []
        self.path_cost = path_cost
        self.manhatten_dist = manhatten_dist

def find_index(grid, num):
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == num: return y, x
    print('Error- num not in goal grid')
    return None

def get_manhatten_dist(curr_state, goal_state, depth):
    # go through each one and for each one check it's corresponding
    man_dist = 0
    for y in range(len(curr_state)):
        for x in range(len(curr_state)):
            goal_index = find_index(goal_state, curr_state[y][x])

            dist = abs(y - goal_index[0]) + abs(x - goal_index[1]) # dist = sum of abs diff of indexes
            man_dist += dist
    return man_dist + depth

# returns the positions for both blanks
# index 0 - position of first blank 
# index 2 - position of second blank
def get_blank_positions(grid):
    positions = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                positions.append([i, j])
            if len(positions)==2: break
    return positions

# new_pos is good if the next step is not out of range
# next step can replace a blank only if the corressponding blank can move as well
# not out of range
def is_new_pos(new_pos, state, new_index):
    if new_pos < 0 or new_pos > 3:
        return False
    elif state[new_index[0]][new_index[1]] == 0:
        return False
    return True

# returns the new_state
# i = action
# b = blank position
def apply_actions(i, node, b, res_state):
    if i == 'L':
        if b[1] - 1 >= 0:
            num = res_state[b[0]][b[1] - 1]
            # move blank to left
            res_state[b[0]][b[1]-1] = 0
            # move num to right (curr_pos)
            res_state[b[0]][b[1]] = num   
    elif i == 'R':
        if b[1] + 1 <= 3:
            num = res_state[b[0]][b[1] + 1]
            # move blank to right
            res_state[b[0]][b[1]+1] = 0
            # move num to left (curr_pos)
            res_state[b[0]][b[1]] = num   
    elif i == 'U':
        if b[0] - 1 >= 0:
            num = res_state[b[0] - 1][b[1]]
            # move blank up
            res_state[b[0]-1][b[1]] = 0
            # move num down (curr_pos)
            res_state[b[0]][b[1]] = num 
    elif i == 'D': 
        if b[0] + 1 <= 3:
            num = res_state[b[0] + 1][b[1]]
            # move blank down
            res_state[b[0]+1][b[1]] = 0
            # move num up (curr_pos)
            res_state[b[0]][b[1]] = num 
    return res_state

# return the children of all possible states
def get_states(blank_pos, node):
    # get multiple states for actions
    # move the first blank first, followed by 2nd
    # do a nested for loop for each possible action: LL, LR, etc.
    # if LL------
    b1_x = blank_pos[0][1]
    b1_y = blank_pos[0][0]
    b2_x = blank_pos[1][1]
    b2_y = blank_pos[1][0]

    actions = ['L', 'R', 'U', 'D']
    state_lst = []
    node_state = node.state
    for i in actions:
        for j in actions:
            # create deep copy of node state
            res_state = []
            for row in node_state:
                res_state.append(row[:])

            if i == 'L' and j == 'L':
                # blanks are next to each other and
                # if b1_x or b2_x is not on edge
                if (res_state[b1_y][b2_x - 1] == 0) and (b1_x - 1 >= 0 and b2_x -1 >= 0):  
                    # print('b1_x', b1_x, ';b2_x', b2_x)
                    num = res_state[b1_y][b1_x-1]
                    res_state[b1_y][b1_x-1] = 0
                    res_state[b1_y][b1_x] = 0
                    res_state[b1_y][b1_x+1] = num
                    state_lst.append(res_state)
                else:
                    # move first blank to the left
                    if b1_x -1 >= 0:
                        num = res_state[b1_y][b1_x-1]
                        res_state[b1_y][b1_x-1] = 0
                        res_state[b1_y][b1_x] = num
                    # move second blank to the left
                    if b2_x -1 >= 0:
                        num = res_state[b2_y][b2_x-1]
                        res_state[b2_y][b2_x-1] = 0
                        res_state[b2_y][b2_x] = num
            elif i == 'R' and j == 'R':
                # blanks are next to each other
                if  (res_state[b1_y][b2_x - 1] == 0) and (b2_x + 1 <= 3 and b1_x +1 <= 3): 
                    num = res_state[b2_y][b2_x+1]
                    res_state[b2_y][b2_x+1] = 0
                    res_state[b2_y][b2_x] = 0
                    res_state[b2_y][b2_x-1] = num 
                    state_lst.append(res_state)
                else:
                    # move second blank to the right
                    if b2_x +1 <= 3:
                        num = res_state[b2_y][b2_x+1]
                        res_state[b2_y][b2_x+1] = 0
                        res_state[b2_y][b2_x] = num
                    # move first blank to the right
                    if b1_x +1 <= 3:
                        num = res_state[b1_y][b1_x+1]
                        res_state[b1_y][b1_x+1] = 0
                        res_state[b1_y][b1_x] = num
            elif i == 'U' and j == 'U':
                # blanks are next to each other
                if  (res_state[b2_y-1][b2_x] == 0) and (b1_y - 1 >= 0 and b2_y - 1 >= 0): 
                    num = res_state[b1_y-1][b1_x]
                    res_state[b1_y-1][b1_x] = 0
                    res_state[b1_y][b1_x] = 0
                    res_state[b1_y+1][b1_x] = num 
                    state_lst.append(res_state)
                else:
                    # move first blank up
                    if b1_y -1 >= 0:
                        num = res_state[b1_y-1][b2_x]
                        res_state[b1_y-1][b1_x] = 0
                        res_state[b1_y][b1_x] = num
                    # move second blank up
                    if b2_y -1 >= 0:
                        num = res_state[b2_y-1][b1_x]
                        res_state[b2_y-1][b1_x] = 0
                        res_state[b2_y][b1_x] = num
            elif i == 'D' and j == 'D':
                # blanks are next to each other; first blank ontop of the second one
                if (res_state[b2_y-1][b2_x] == 0) and (b2_y + 1 <= 3 and b1_y +1 <= 3): 
                    num = res_state[b2_y+1][b2_x]
                    res_state[b2_y+1][b2_x] = 0
                    res_state[b2_y][b2_x] = 0
                    res_state[b2_y-1][b1_x] = num 
                    state_lst.append(res_state)
                else:
                    # move second blank down
                    if b2_y + 1 <= 3:
                        num = res_state[b2_y+1][b2_x]
                        res_state[b2_y+1][b1_x] = 0
                        res_state[b2_y][b1_x] = num
                    # move first blank down
                    if b1_y + 1 <= 3:
                        num = res_state[b1_y+1][b1_x]
                        res_state[b1_y+1][b1_x] = 0
                        res_state[b1_y][b1_x] = num
            else:
                # change first blank first
                res_state = apply_actions(i, node, (b1_y, b1_x), res_state)
                # change second blank
                res_state = apply_actions(j, node, (b2_y, b2_x), res_state)
            state_lst.append(res_state)
    return state_lst

def main(file_name):
    '''
    test grid
    '''
    i_grid = [0]*4
    for i in range(len(i_grid)):
        i_grid[i] = [0] * 4

    for i in i_grid:
        print(i)

    '''
    Extract data from file
    '''
    with open(file_name) as f:
        lines = f.readlines()

    # strip \n from the rows
    for i in range(len(lines)):
        lines[i] = lines[i].strip() # gets rid of any \n

    
    print(lines)
    initial_state = []
    goal_state = []
    change_flag = 0
    for line in lines:
        # empty line seperates input from goal state
        if line == '': 
            change_flag = 1
            continue
        if change_flag:
            row = line.split(' ')
            for i in range(len(row)):
                row[i] = int(row[i])
            goal_state.append(row)
        else:
            row = line.split(' ')
            for i in range(len(row)):
                row[i] = int(row[i])
            initial_state.append(row)
    
    print('initial:')
    for i in initial_state:
        print(i)
    print('final:')
    for i in goal_state:
        print(i)

    frontier = [] 
    explored = []
    nodes = []
    '''
    1- Nodes to store states
    2- In each node we have the map representation, depth, and its children
    3- explored is a list of nodes - have to compare each map of the node 
    4- def move() - loop to add all possible states that are not in explored
    5- function to calculate the manhatten distance
    '''
    man_dist = get_manhatten_dist(initial_state, goal_state, 0)
    root = Node(initial_state, None, None, 0, 0, man_dist)
    frontier.append(root)
    # function to add actions and put into lst
    # check manhatten dsitance of lst and check which has the smallest manhatten distance
    # proceed with that one- make its children and add to lst
    # repeat until chosen state == goal state
    depth = 0
    counter= 0 
    while len(frontier) != 0:
        print('counter:', counter, '----------------------------')
        # search for node with lowest manhatten distance
        node = frontier[0]
        count = 0
        index = 0
        for i in frontier:
            if i.manhatten_dist < node.manhatten_dist:
                index = count
                node = i 
            count += 1

        # add state to explored
        explored.append(node.state)
        nodes.append(node)

        if node.state == goal_state:
            print('done')
            break
    
        # pop node 
        # swap node with lowest man dist with last index and pop
        frontier[index], frontier[-1] = frontier[-1], frontier[index] 
        node = frontier.pop()
        
        # get index of blank states
        blank_pos = get_blank_positions(node.state)
        # print(blank_pos)
        b1 = blank_pos[0]
        b2 = blank_pos[1]

        children = get_states(blank_pos, node)
        # print('curr_state:------------------')
        # print('man_dis:', i.manhatten_dist)
        # print('depth:', i.depth)
        # for row in i.state:
        #     print(row)
        
        # print('---')

        action = 'T, T'
        # make each map into a node
        for grid in children:
            if grid not in explored:
                man_dist = get_manhatten_dist(grid, goal_state, i.depth+1)
                frontier.append(Node(grid, i, action, i.depth+1, 0, man_dist))
                # print('man_dis-----',man_dist)
                # print('depth:', frontier[-1].depth)
                # x = frontier[-1].state
                # for z in x:
                #     print(z)
        counter += 1
        # if counter == 200: 
        #     break
    return nodes[-1]
        
x = main('input2.txt')
print('final-------')
for row in x.state:
    print(row)
print('depth-----')
print(x.depth)
print('man_dis:', x.manhatten_dist)


        



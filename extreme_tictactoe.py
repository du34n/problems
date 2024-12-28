# -- coding: utf-8 --
"""
Created on Thu Mar 21 18:21:12 2024

@author: gencyetenek
"""

import math
import copy
######################################################################################################################################################
def value(current_state):
    n = len(current_state)
    points_1 = 0
    for row in current_state:
        consecutive_marks = 0
        for cell in row:
            if cell == 1:
                consecutive_marks += 1
            else:
                if consecutive_marks > 1:
                    points_1 += sum(range(1, consecutive_marks + 1))
                consecutive_marks = 0
        if consecutive_marks > 1:
            points_1 += sum(range(1, consecutive_marks + 1))
    for j in range(n):
        consecutive_marks = 0
        for i in range(n):
            if current_state[i][j] == 1:
                consecutive_marks += 1
            else:
                if consecutive_marks > 1:
                    points_1 += sum(range(1, consecutive_marks + 1))
                consecutive_marks = 0
        if consecutive_marks > 1:
            points_1 += sum(range(1, consecutive_marks + 1))
    n = len(current_state)
    points_2 = 0
    for row in current_state:
        consecutive_marks = 0
        for cell in row:
            if cell == 2:
                consecutive_marks += 1
            else:
                if consecutive_marks > 1:
                    points_2 += sum(range(1, consecutive_marks + 1))
                consecutive_marks = 0
        if consecutive_marks > 1:
            points_2 += sum(range(1, consecutive_marks + 1))
    for j in range(n):
        consecutive_marks = 0
        for i in range(n):
            if current_state[i][j] == 2:
                consecutive_marks += 1
            else:
                if consecutive_marks > 1:
                    points_2 += sum(range(1, consecutive_marks + 1))
                consecutive_marks = 0
        if consecutive_marks > 1:
            points_2 += sum(range(1, consecutive_marks + 1))
    return points_1 - points_2
########################################################################################################################
def terminal(board):
    count = 0
    for row in board:
        for element in row:
            if element == 0:
                count = count + 1
    return count == 0
########################################################################################################################
def player():
    global initial_1s, initial_2s, turns_list,current_place

    result_for_player = turns_list[current_place]
    current_place = current_place + 1

    return result_for_player
########################################################################################################################
def actions(board):
    actions_list = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                actions_list.append([row, column])

    return actions_list
########################################################################################################################
def result(board, action, turn):
    board_t = copy.deepcopy(board)
    for row in range(len(board)):
        for column in range(len(board[row])):
            if row == action[0] and column == action[1]:
                board_t[row][column] = turn
    return board_t
########################################################################################################################
def turns_ordered(total_number_of_1_s, total_number_of_2_s, board, timeout_1=0, timeout_2=0):
    ordered_list_of_turns = []

    ordered_list_of_turns.extend([1] * (timeout_1 + 1))
    total_number_of_1_s = total_number_of_1_s - 1

    ordered_list_of_turns.extend([2] * (timeout_2 + 1))
    total_number_of_2_s = total_number_of_2_s - 1

    while total_number_of_1_s > 0 or total_number_of_2_s > 0:
        if total_number_of_1_s > 0:
            ordered_list_of_turns.append(1)
            total_number_of_1_s = total_number_of_1_s - 1
        if total_number_of_2_s > 0:
            ordered_list_of_turns.append(2)
            total_number_of_2_s = total_number_of_2_s - 1
    arranged_list = []

    for i in range(count_Zeros(board)):
        arranged_list.append(ordered_list_of_turns[i])

    return arranged_list
########################################################################################################################
def number_of_1s_to_be_placed(timeout_1, timeout_2, available_spaces):
    if available_spaces == 1:
        return 1
    elif timeout_1 + 1 >= available_spaces:
        return available_spaces
    elif timeout_2 >= available_spaces:
        return 1
    elif timeout_1 + 1 + timeout_2 >= available_spaces:
        return timeout_1 + 1
    available_spaces = available_spaces - timeout_1 - timeout_2
    if available_spaces % 2 == 0:
        number_of_1s = available_spaces / 2
    if available_spaces % 2 == 1:
        number_of_1s = (available_spaces + 1) / 2
    if number_of_1s == 0:
        number_of_1s = 1
    return number_of_1s
########################################################################################################################
def count_Zeros(board):
    count = 0
    for row in board:
        for element in row:
            if element == 0:
                count = count + 1
    return count


########################################################################################################################
def count_1s(board):
    count = 0
    for row in board:
        for element in row:
            if element == 1:
                count = count + 1
    return count
########################################################################################################################
def count_2s(board):
    count = 0
    for row in board:
        for element in row:
            if element == 2:
                count = count + 1

    return count
########################################################################################################################
def perfect_case(board_input, a, b,turn_list):
    if terminal(board_input):
        return value(board_input)

    if turn_list[0] == 1:
        max_val = -math.inf
        for move in actions(board_input):
            child = result(board_input, move, 1)
            temporary = perfect_case(child,a ,b,turn_list[1:])
            max_val = max(max_val, temporary)
            a = max(max_val,a)
            if b <= a:
                break
        return max_val
    else:
        min_val = math.inf
        for move in actions(board_input):
            child = result(board_input, move, 2)
            temporary = perfect_case(child,a , b, turn_list[1:])
            min_val = min(min_val, temporary)
            b = min(min_val,b)
            if b <= a:
                break
        return min_val
########################################################################################################################
n_grid, timeout_1, timeout_2 = map(int, input().split())
row = []
for i in range(n_grid):
    curr_row = input()[:]
    row.append(curr_row)

board_input = [[int(char) for char in item] for item in row]

player_1_count_of_turns_without_timeout_1 = number_of_1s_to_be_placed(timeout_1, timeout_2, count_Zeros(board_input))
turns_list = turns_ordered(player_1_count_of_turns_without_timeout_1,
                           count_Zeros(board_input) - player_1_count_of_turns_without_timeout_1, board_input, timeout_1, timeout_2)
initial_1s = count_1s(board_input)
initial_2s = count_2s(board_input)
current_place = 0

final_val = perfect_case(board_input,-math.inf, math.inf,turns_list)
if final_val > 0:
    print("yes")
else:
    print("no")
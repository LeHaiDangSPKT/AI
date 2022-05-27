#  Tham khảo phần code của thầy And_or_search_8queen.py
from collections import deque
import tkinter as tk 
import numpy as np
import time 
import LeHaiDang_20110243_tuan08_NQueensProblem as NQueensProblem

def StateToBoard(state):
    '''Dùng để chuyển từ mảng 1 chiều sang mảng 2 chiều, để dễ biểu diễn trên ChessBoard'''
    a = np.zeros((no_of_queens, no_of_queens)) #Tạo mảng 2D có kích thước no_of_queens x no_of_queens
    for i in range(no_of_queens):
        a[state[i], i] = -1  #Tại các hàng đặt quân hậu (state[i]) ứng với từng cột i, đánh dấu = -1 để vẽ đồ họa
    return a

def ShowSolution(state, is_init):
    '''Dùng để tạo ra giao diện cho ChessBoard'''
    board = StateToBoard(state)
    for r in range(no_of_queens):
        for c in range(no_of_queens):
            if is_init:
                label.append(tk.Label(frame, bd = 0.5, relief = "solid", width = 4, height = 2))
            color = "white"
            if r%2 == c%2:
                color = "gray"
            if board[r][c] == -1:
                color = "red"
            label[no_of_queens*r + c].grid(row = r, column = c)
            label[no_of_queens*r +c].config(bg = color)

def and_or_graph_search(problem):
    '''
    Thuật toán AND-OR-SEARCH (AO*) dùng để tìm lời giải cho các bài toán N quân hậu
    Hàm and_or_graph_search() sử dụng đệ quy tương hỗ, dựa trên Depth-First Search để tìm Goal-state
    Sử dụng 2 hàm con, gọi đệ quy lẫn nhau là or_search() và and_search()
    '''

    def or_search(state, problem, path):
        '''
        Return: None nếu Failure
        state: state hiện tại, là một tuple chứa trạng thái của các quân hậu trên bàn cờ
        problem: là thể hiện (instance) của NQUEENSPROBLEM
        path: đường đi của state hiện tại
        '''
        if problem.goal_test(state):
            print(state)
            ShowSolution(state, False)
            window.update()
            return []
        if state in path:
            return None
        actions = problem.actions(state)

        plans = []
        for action in actions:
            plan = and_search([problem.result(state, action)], problem, [state]+path)
            '''Nếu tìm thấy goal-state thì mỗi action chỉ ứng với 1 goal-state nên ta appen vào plans để có nhiều goal-state'''
            if plan is not None:
                plans.append((action, plan))
        if len(plans) > 0:
            return plans
        return None
    
    def and_search(states, problem, path):
        '''
        Return dictionary là các plan nếu có thể tìm thấy ít nhất một goal-state ứng với state s_i. Ngược lại return None (Failure)
        state: list các states (chính là các successor của state hiện tại ở or_search())
        problem: thể hiện (instance) của NQUEENSPROBELEM
        path: đường đi của state hiện tại
        '''

        plans = {}

        '''Thêm các phần tử vào plan'''
        for state in states:
            plan = or_search(state, problem, path)
            if plan is None:
                continue
            else:
                plans[state] = plan
        
        '''Có thể sau khi chuẩn hóa dictionary plans thì không còn phần từ nào. Tức là từ state ở or_search(), sinh ra các successors, không có một successors nào đi đến goal-state'''
        if len(plans) > 0:
            return plans
        else:
            return None
    
    state = problem.initial
    plans = {}
    plans[state] = or_search(state, problem, [])
    return plans

def ListGoalState(dictionary):
    for key in dictionary:
        array = dictionary.get(key)
        if array == []:
            goalStates.append(key)
        else:
            for i in dictionary.get(key):
                action, plan = i
                ListGoalState(plan)


if __name__ == '__main__':
    no_of_queens = 15
    problem = NQueensProblem.NQueensProblem(no_of_queens)

    #--------------------------------------------

    window = tk.Tk()
    window.title("N - Queens")
    window.geometry("600x650+500+50")

    frame = tk.Frame(window, bd = 0.5, relief="solid")
    frame.place(x = 60, y = 60)

    label = []
    
    ShowSolution(problem.initial, True)
    window.update()

    ####################
    start = time.time()
    result = and_or_graph_search(problem)
    total = time.time() - start
    print(result)

    goalStates = deque()
    if (result is not None) and (not any(result.get(key) == None for key in result)):
        ListGoalState(result)

    print("No. goal states: ", len(goalStates))
    print("Time: ", total, end="\n\n")

    #Tạo và lưu kết quả vào file
    with open("LeHaiDang_20110243_tuan08_output.txt", "w") as f:
        print(len(goalStates), file = f, end="\n\n")
        print("Time: ", total, file = f, end="\n\n")
        for goal in goalStates:
            print(goal, file = f)
        print(result, file = f, end="\n\n")
    f.close()
    window.mainloop()


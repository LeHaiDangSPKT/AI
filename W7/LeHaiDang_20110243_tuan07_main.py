# Solve N-queens problems using Simulated annealing algorithm
#  Tham khảo phần giao diện: https://youtu.be/7w8jk0r4lxA
#  Tham khảo phần code của thầy Simulated_annealing.py

import numpy as np
import random
import itertools 
import math
import tkinter as tk 
import time 
import LeHaiDang_20110243_tuan07_Node as Node
import LeHaiDang_20110243_tuan07_NQueensProblem as NQueensProblem

def schedule(t, k=20, lam=0.005, limit=1000):
    """One possible schedule function for simulated annealing"""
    return (k * np.exp(-lam * t) if t < limit else 0) 

def simulated_annealing(problem):
    current = Node.Node(problem.initial)
    for t in itertools.count(start = 1):
        T = schedule(t)
        if (T == 0):
            return current.state
        
        sucessors = current.expand(problem)
        if len(sucessors) == 0:                         #Không thể đặt thêm quân hậu nào nữa
            if current.state.count(-1) > 0:             #Khi vẫn còn cột cần phải đặt quân hậu
                current = Node.Node(problem.initial)    #Random lại từ đầu, để có solution khác
        else:
            next = random.choice(sucessors)             #Chọn ngẫu nhiên 1 successor trong tập được expand từ node hiện tại
            deltaE = problem.value(next) - problem.value(current)
            if deltaE > 0:
                current = next
            elif random.uniform(0.0, 1.0) < math.exp(deltaE/T):
                current = next
def StateBoard(state):
    '''Dùng để chuyển từ mảng một chiều thành mảng hai chiều -> Biểu diễn trên ChessBoard'''
    a = np.zeros((no_of_queens, no_of_queens))
    for i in range(no_of_queens):
        a[state[i], i] = -1     #Tại các hàng đặt quân hậu (state[i]) ứng với từng cột i, đánh dấu -1 để vẽ lên đồ họa
    return a
def InitChessBoard(state):
    board = StateBoard(state)
    for r in range(no_of_queens):
        for c in range(no_of_queens):
            label.append(tk.Label(frame, bd = 0.5, relief="solid", width=4, height=2 ))
            color = "white"
            if r%2 == c%2:
                color = "gray"
            if board[r][c] == -1:
                color = "red"
            label[no_of_queens*r + c].grid(row = r, column = c)
            label[no_of_queens*r + c].config(bg = color)
def Solve():
    begin = time.time()
    result = simulated_annealing(problem) 
    totalTime = time.time() - begin

    print(result)
    InitChessBoard(result)      #Hiển thị lê giao diện
    labelTime.config(text = 'Total time: ' + str(totalTime) + 'sec.')
def SolveEvent(event):
    Solve()

if __name__ == '__main__':
    no_of_queens = 15
    problem = NQueensProblem.NQueensProblem(no_of_queens)
   
    #Window
    window = tk.Tk()
    window.title("15 - QUEENS")
    window.geometry("600x650+300+50")

    #Frame
    frame = tk.Frame(window, bd = 0.5, relief = 'solid')
    frame.place(x = 60, y = 60)

    #Label
    label = []
    #Button 
    button = tk.Button(window, text="Giải", bg = 'gray', width=8, relief='raised', bd = 1)
    button.place(x = 60, y = 610)
    button.bind('<Button-1>', SolveEvent)

    #LableTime
    labelTime = tk.Label(window)
    labelTime.place(x=160, y=610)

    Solve()

    window.mainloop()


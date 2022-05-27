#Tham khảo:
#Thuật toán: 
#    - file code Searching02.py của thầy
#    - Pseudocode: (slide) https://cse.sc.edu/~mgv/csce580f08/gradPres/clevelandWaggonerAstar080915.pdf
#    - Pseudocode: (video) https://youtu.be/wEDCJZWZLnA?t=3299
#    - Hàm Heuristics: http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html#diagonal-distance


import time 
import tkinter as tk
import LeHaiDang_20110243_tuan06_Astar as Astar
if __name__ == "__main__":
    maze =     [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],  # 1: obstacle position
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
    start = (0, 0)
    goal = (8, 9)

    begin = time.time()
    path = Astar.astar(maze, start, goal)
    print("Path:", path)
    print("Len(Path) = ", len(path))
    totalTime = time.time() - begin

    #----------------------------------------------------------
    #GUI

    #window
    window = tk.Tk()
    window.title("MAZE")
    window.geometry("400x400+200+200")

    #frame
    frame = tk.Frame(window, bd = 0.5, relief = "solid")
    frame.place(x = 85, y = 80)

    #Title
    labelTitle = tk.Label(window, text = "MÊ CUNG", fg = "Red", font = ("Arial Bold", 30))
    labelTitle.place(x = 100, y = 10)

    #Maze
    label = []
    for i in range(0,100):
        (x, y) = (i//10, i%10)
        color = "cyan"
        label.append(tk.Label(frame, bd = 0.5, bg = color, relief = "solid", height = 1, width = 2, font = ("Arial Bold", 12)))
        label[i].grid(row = x, column = y)
        if maze[x][y] == 1:
            label[i].config(bg = "black")
    #Thay doi bgcolor cho start_node va end_node
    label[start[0]*10 + start[1]].config(bg = "Red")
    label[goal[0]*10 + goal[1]].config(bg = "Red")

    index = 0
    def PrintPath(event):
        '''
        Dùng để in đường đi ở mỗi step
        '''
        global index
        if (index < len(path)):
            (r, c) = path[index]
            label[10*r + c].config(bg = "Yellow")
            index += 1
        else:
            labelTime = tk.Label(window, text = "Total time: " + str(totalTime) + " sec.")
            labelTime.place(x = 90, y = 360)

    #Button
    button = tk.Button(window, text = ">>>", width = 8)
    button.place(x = 160, y = 320)
    #su kien click cho button
    button.bind("<Button-1>", PrintPath)


    window.mainloop()
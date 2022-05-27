from anyio import current_effective_deadline
import LeHaiDang_20110243_tuan06_Node as Node
def astar(maze, start, end):
    #Khởi tạo các node start và end
    start_node = Node.Node(position=start)
    end_node = Node.Node(position=end)

    #Khởi tạo open_list và closed_list
    open_list = []
    closed_list = []

    #Thêm start_node vào open_list
    open_list.append(start_node)

    while len(open_list) > 0:   #Khi open_list không rỗng
        current_node = open_list[0]
        current_index = 0

        #Tìm node có hàm f nhỏ nhất có trong open_list
        for (index, node) in enumerate(open_list):
            if node.f < current_node.f:
                current_index = index
                current_node = node
        
        open_list.pop(current_index)
        closed_list.append(current_node)

        #Kiểm tra current_node có phải là end_node không
        if current_node == end_node:
            #Tạo biến path chứa đường đi từ start_node đến gold_node
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] #Đảo ngược mảng
        
        else:
            children = current_node.ChildNode(maze)
            for child in children:
                #Tính giá trị f,g,h của child_node
                child.g = current_node.g +1
            #Hàm Heuristic tính theo thuật toán Chebyshev distance tham khảo tại: http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html#diagonal-distance

                dx = abs(child.position[0] - end_node.position[0])
                dy = abs(child.position[1] - end_node.position[1])

                def Check(list):
                    '''
                    Dùng để kiểm tra xem child đã có trong list hay chưa, nếu có mà child.g nhỏ hơn (tức là đường đi child có chi phí thấp hơn) thì replace đường đi cũ bằng đường đi mới (di qua node child)
                    '''
                    for index, node in enumerate(list):
                        if node == child and node.g > child.g:
                            list.pop(index)
                            open_list.append(child)
                            return
                
                #Kiểm tra child node
                if child not in open_list and child not in closed_list:
                    open_list.append(child)
                elif child in open_list:
                    Check(open_list)
                elif child in closed_list:
                    Check(closed_list)
                else:
                    continue


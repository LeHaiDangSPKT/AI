class Node:
    '''
    Mỗi node gồm các thông tin:
        + Position: node tọa độ trong mê cung
        + Parent: node cha của node hiện tại
        + f: hàm lượng giá
        + g: độ dài quãng đường thực tế từ node bắt đầu đến node hiện tại
        + h: hàm Hẻuistic ước lượng khoảng cách từ node hiện tại đến node đích, theo thuật toán Chebyshev distance
    '''

    def __init__(self, position, parent = None, f_Value = 0, g_Value = 0, h_Value = 0):
        self.position = position
        self.parent = parent
        self.f = f_Value
        self.g = g_Value
        self.h = h_Value
    
    def __eq__(self, other):
        '''Dùng để so sánh 2 node'''
        return self.position == other.position
    
    def ChildNode(self, maze):
        '''
        Dùng để sinh ra các node của của node hiện tại
        Maze: là ma trận chứa mê cung
        '''

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            #Lấy vị trí của node
            node_position = (self.position[0] + new_position[0], self.position[1] + new_position[1])

            #Kiểm tra position của node có hợp lệ hay không (tức là có nằm trong maze không)
            if node_position[0] < 0 or node_position[0] > (len(maze) - 1) or node_position[1] < 0 or node_position [1] > (len(maze[len(maze) - 1]) - 1):
                continue

            #Kiểm tra có đi nhầm ô chứa vật cản hay không
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            #Tạo node mới
            new_node = Node(position = node_position, parent = self)
            
            #Them new_node vào children
            children.append(new_node)
        return children
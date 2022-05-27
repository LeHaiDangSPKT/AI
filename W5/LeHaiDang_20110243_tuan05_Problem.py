import LeHaiDang_20110243_tuan05_Search as Search
class Problem:
    '''
    Dùng để chứa thông tin về Proble 8-puzzle
    InitialState: trạng thái khởi tạo của puzzle
    GoalState: trạng thái đích của puzzle
    '''

    import queue
    Actions = queue.LifoQueue()         #chứa các action trong quá trình tìm kiếm
    SavedStates = queue.LifoQueue()     #Chứa các state trong quá trình tim kiếm
    nameActions = {-3: 'UP', -1: 'LEFT', 1: 'RIGHT', 3: 'DOWN'}

    def __init__(self, initialState, goalState = [0,1,2,3,4,5,6,7,8]):
        self.InitialState = initialState
        self.GoalState = goalState
        
    def GoalTest(self, node):
        '''Kiểm tra node.State có phải là GoalState không'''
        return node.State == self.GoalState
    
    def Solution(self):
        '''Được gọi khi GoalState(node) = true'''
        return self.Actions.queue[:], self.SavedStates.queue[:]

    def Action(self, node):
        '''Sinh ra các action tương ứng cho mỗi node'''
        Act = []
        index = node.State.index(0)
        if (index - 3 >= 0):
            Act.append(-3)
        if (index + 3 <= 8):
            Act.append(3)
        if (index - 1 >= 0 and (index//3 == (index - 1)//3)):
            Act.append(-1)
        if (index + 1 <= 8 and (index//3 == (index + 1)//3)):
            Act.append(1)

        return Act
    
    def Solve(self):
        '''Hàm được gọi để giải problem'''
        act, states = Search.IDS(self)
        actions = [self.nameActions[x] for x in act]
        return actions, states

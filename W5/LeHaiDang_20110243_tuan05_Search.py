import itertools
import LeHaiDang_20110243_tuan05_Node as Node

def IDS(problem):
    '''Iteractive Deepening Search'''
    def Recursive_DLS(node, problem, limit):
        if (problem.GoalTest(node)):
            return problem.Solution()
        elif limit == 0:
            return 0
        else:
            cutoff_occured = False
            for action in problem.Action(node):
                child = node.ChildNode(action)
                problem.Actions.queue.append(action)
                problem.SavedStates.queue.append(child.State)
                result = Recursive_DLS(child, problem, limit - 1)
                if result == 0:
                    cutoff_occured = True
                    problem.Actions.queue.pop()
                    problem.SavedStates.queue.pop()
                elif result != -1:
                    return result
            if cutoff_occured:
                return 0
            else:
                return -1


    for depth in itertools.count():
        rootNode = Node.Node(problem.InitialState)
        result = Recursive_DLS(rootNode, problem, depth)
        if result != 0:
            return result

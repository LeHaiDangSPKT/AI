

class NQueensProblem:
    """The problem of placing N queens on an NxN board with none attacking each other. 
    A state is represented as an N-element array, where a value of r in the c-th entry means there is a queen at column c,
    row r, and a value of -1 means that the c-th column has not been filled in yet. We fill in columns left to right.
    
    Sample code: iterative_deepening_search(NQueensProblem(8))
    Result: <Node (0, 4, 7, 5, 2, 6, 1, 3)>
    """

    def __init__(self, N):
        #self.initial = initial 
        self.initial = tuple([-1]*N)  # -1: no queen in that column
        self.N = N

    def actions(self, state):
        """In the leftmost empty column, try all non-conflicting rows."""
        if state[-1] is not -1:
            return []  # All columns filled; no successors
        else:
            col = state.index(-1)
            #return [(col, row) for row in range(self.N)
            return [row for row in range(self.N)
                    if not self.conflicted(state, row, col)]

    def goal_test(self, state):
        """Check if all columns filled, no conflicts."""
        if state[-1] is -1:
            return False
        return not any(self.conflicted(state, state[col], col)
                       for col in range(len(state)))

    def result(self, state, row):
        """Place the next queen at the given row."""
        col = state.index(-1)
        new = list(state[:])
        new[col] = row
        return tuple(new)

    def conflicted(self, state, row, col):
        """Would placing a queen at (row, col) conflict with anything?"""
        return any(self.conflict(row, col, state[c], c)
                   for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
        return (row1 == row2 or  # same row
                col1 == col2 or  # same column
                row1 - col1 == row2 - col2 or  # same \ diagonal
                row1 + col1 == row2 + col2)  # same / diagonal

    def value(self, node): 
        """Return (-) number of conflicting queens for a given node"""
        num_conflicts = 0
        for (r1, c1) in enumerate(node.state):
            for (r2, c2) in enumerate(node.state):
                if (r1, c1) != (r2, c2):
                    num_conflicts += self.conflict(r1, c1, r2, c2)

        return -num_conflicts 
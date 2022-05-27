# Tham khảo code của thầy CSP_AC3.py
# Em có tách ra thành nhiều lớp để tiện quản lý code

import LeHaiDang_20110243_tuan10_Utilities as Utilities
import LeHaiDang_20110243_tuan10_Sudoku as Sudoku

## Constraint Propagation with AC3
''' IMPLEMENT THE FOLLOWING FUNCTION '''
def AC3(csp):
    """See [Figure 6.3] for the algorithm"""
    queue = {(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]}
    csp.curr_domains = csp.domains.copy() # curr_domains: a copy of domains. We will do inference on curr_domains
    
    ''' ADD YOUR CODE HERE '''
    while (len(queue)): #queue không rỗng
        (Xi, Xj) = queue.pop()
        if revise(csp, Xi, Xj):
            if len(csp.domains[Xi]) == 0:   #Nếu kích thước của Di = 0
                return False
            for Xk in csp.neighbors[Xi]:
                if Xk is not Xj:
                    queue.add((Xk, Xi)) 
    return True  # CSP is satisfiable


def revise(csp, Xi, Xj):
    """Return true if we remove a value."""
    revised = False
    for x in csp.domains[Xi]: 
        conflict = True
        
        for y in csp.curr_domains[Xj]:
            if csp.constraints(Xi, x, Xj, y):
                conflict = False
                break
        if conflict:
            csp.domains[Xi].remove(x)
            revised = True
                
    return revised
    
# CSP Backtracking Search  
# Variable ordering
def first_unassigned_variable(assignment, csp): #random selection
    """The default variable order."""
    return Utilities.first([var for var in csp.variables if var not in assignment])

def num_legal_values(csp, var, assignment):
    if csp.curr_domains:
        return len(csp.curr_domains[var])
    else:
        return Utilities.Utilities.count(csp.nconflicts(var, val, assignment) == 0 for val in csp.domains[var])

def minimum_remaining_values(assignment, csp):
    """Minimum-remaining-values heuristic."""
    return Utilities.Utilities.argmin_random_tie([v for v in csp.variables if v not in assignment],
                             key=lambda var: num_legal_values(csp, var, assignment))

# Value ordering
def unordered_domain_values(var, assignment, csp): #random selection
    """The default value order."""
    return (csp.curr_domains or csp.domains)[var]

def least_constraining_value(var, assignment, csp):
    """Least-constraining-values heuristic."""
    return sorted((csp.curr_domains or csp.domains)[var], key=lambda val: csp.nconflicts(var, val, assignment))   

# Inference
def forward_checking(csp, var, value, assignment, removals):
    """Prune neighbor values inconsistent with var=value."""
    for B in csp.neighbors[var]:
        if B not in assignment:
            for b in csp.curr_domains[B][:]:
                if not csp.constraints(var, value, B, b):
                    csp.curr_domains[B].remove(b)
                    if removals is not None:
                        removals.append((B, b)) # variable B and value b are removed from its domain
            if not csp.curr_domains[B]:
                return False
    return True
 

''' READ AND COMMENT to show your comprehensive understanding of the following function '''
# Backtracking search
def backtracking_search(csp, select_unassigned_variable=minimum_remaining_values,
                        order_domain_values=least_constraining_value, 
                        inference=forward_checking):
    """See [Figure 6.5] for the algorithm"""       

    def backtrack(assignment):   
        #Tất cả variables của csp đều được gán giá trị nên return solution
        if len(assignment) == len(csp.variables):
            return assignment

        #Chọn ra một giá trị var gán cho variable (variable chưa gán giá trị) (minimum_remaining_values, một hàm heuristic)
        var = select_unassigned_variable(assignment, csp)

        #Lấy mỗi giá trị từ domain
        for value in order_domain_values(var, assignment, csp):
            #Với môi value được chọn từ domain, nếu không bị trùng với bất kỳ một giá trị nào khác cùng hàng/cột/cùng box 3x3
            if 0 == csp.nconflicts(var, value, assignment):
                #Thì value đó "có thể" được gán cho variable hiện tại
                csp.assign(var, value, assignment)      
                removals = [(var, a) for a in csp.curr_domains[var] if a != value]   #Chứa các giá trị bị lược bỏ khỏi domain hiện tại curr_domains
                csp.curr_domains[var] = [value] #Giả sử gái trị value là giá trị của var, nên ta gán vào
                #Hàm inference để thu hẹp lại domain của các neighbors
                if inference(csp, var, value, assignment, removals):
                    #Gọi đệ quy hàm Backtrack để tim giá trị của những biến variables còn lại chưa được gán giá trị
                    result = backtrack(assignment)
                    if result is not None:
                        return result
                restore(csp, removals)
        csp.unassign(var, assignment)
        return None
        
    csp.curr_domains = csp.domains.copy()
    result = backtrack({})
    return result

def restore(csp, removals):
    """Undo a supposition and all inferences from it."""
    for B, b in removals:
        csp.curr_domains[B].append(b)

if __name__ == '__main__':       

    # init_assign_easy = '.2...194881.6.......4.276..17..9...33.........48.53.....61....2....74..6.5.9....7'
    # sodoku = Sudoku.Sudoku(init_assign_easy)
    # #print('VARIABLES:');sodoku.display_variables()
    # print('EASY SUDOKU:'); sodoku.display() 
    # AC3(sodoku)
    # print('SOLUTION TO THE EASY SUDOKU:'); sodoku.display()

    init_assign_hard = '.9.............46.2.......5.7.8.4.1..3..2....5...6.8...1.73..2.9.8.5.......2.....'
    sodoku = Sudoku.Sudoku(init_assign_hard)
    print('\nHARD SUDOKU:'); sodoku.display()      
    backtracking_search(sodoku)
    print('SOLUTION TO THE HARD SUDOKU:'); sodoku.display()
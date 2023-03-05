import heapq


class PriorityQueue:
    def __init__(self, items=(), priority_function=(lambda x: x)):
        self.priority_function = priority_function
        self.pqueue = []
        # add the items to the PQ
        for item in items:
            self.add(item)


    """
    Add item to PQ with priority-value given by call to priority_function
    """
    def add(self, item):
        pair = (self.priority_function(item), item)
        heapq.heappush(self.pqueue, pair)

    """
    pop and return item from PQ with min priority-value
    """
    def pop(self):
        return heapq.heappop(self.pqueue)[1]

    """
    gets number of items in PQ
    """
    def __len__(self):
        return len(self. pqueue)

class Node:
    def __init__(self, state, parent_node=None, action_from_parent=None, path_cost=0):
        self.state = state
        self.parent_node = parent_node
        self.action_from_parent = action_from_parent
        self.path_cost = path_cost
        self.depth = 0 if parent_node == None else parent_node.depth + 1

    def __lt__(self, other):
        return self.state < other.state

def expand(problem,node: Node):
    s = node.state
    for action in problem.actions:
        s2 = problem.result(s.actions)
        cost = node.path_cost + problem.action-cost(s,action,s2)
        yield Node(state=s2,parent_node=node,action_from_parent=action,path_cost=cost)
def get_path_actions(node: Node):
    if node == None or node.parent_node == None:
        return []
    return get_path_actions(node=node.parent_node) + list(node)
def get_path_states(node: Node):
    if node == None:
        return []
    return get_path_states(node.parent_node) + list(node.state)
def best_first_search(problem, f):
    node = Node(state=problem.initial)
    frontier = PriorityQueue(items=node,priority_function=f)
    reached = {problem.initial:node}
    while frontier != None:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        for child in expand(problem=problem,node=node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.add(child)
    return None


def best_first_search_treelike(problem, f):
    node = Node(state=problem.initial)
    frontier = PriorityQueue(items=node,priority_function=f)
    # reached = {problem.initial:node}
    while frontier != None:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        for child in expand(problem=problem,node=node):
            s = child.state
            # if s not in reached or child.path_cost < reached[s].path_cost:
            #     reached[s] = child
            frontier.add(child)
    return None

def breadth_first_search(problem,treelike=False):
    if not  treelike:
        best_first_search(problem=problem)
    else:
        best_first_search_treelike(problem=problem)

def depth_first_search(problem,treelike=False):
    if not treelike:
        best_first_search(problem=problem)
    else:
        best_first_search_treelike(problem=problem)

def uniform_cost_search(problem,treelike=False):
    if not treelike:
        best_first_search(problem=problem)
    else:
        best_first_search_treelike(problem=problem)
def greedy_search(problem,h,treelike=False):
    if not treelike:
        best_first_search(problem=problem,f=h)
    else:
        best_first_search_treelike(problem=problem,f=h)
def astar_search(problem,h,treelike=False):
    if not treelike:
        best_first_search(problem=problem,f=( lambda n: n.path_cost + h(n) ))
    else:
        best_first_search_treelike(problem=problem,f=( lambda n: n.path_cost + h(n) ))


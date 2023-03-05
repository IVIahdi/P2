class ConstrainedRouteProblem:
    def __init__(self, initial_agent_loc, goal_loc, map_edges, map_coords, must_visit):
        self.initial_agent_loc = initial_agent_loc
        self.goal_loc = goal_loc
        self.map_edges = map_edges
        self.map_coords = map_coords
        self.must_visit = must_visit
        temp = [False for i in range(len(self.must_visit)+1)]
        self.initial_state = (initial_agent_loc, False, False) + tuple(temp)

    def actions(self, state):
        return [i for i in self.map_edges if state[0] in i]

    def result(self, state, action):
        if action in self.must_visit:
            if action == self.goal_loc:
                self.initial_state[1] == True
                return True
            else:
                return False

    def action_cost(state1, action, state2):
        try:
            return action.map_edges[state2, state1]
        except:
            return action.map_edges[state1, state2]

    def is_goal(self,state):
        return 0
    def h(self,node):
        x = ((self.map_coords[1] - node.state[1])**2 + (self.map_coords[0] - node.state[0])**2)** 0.5
        return x
class GridProblemWithMonsters:
    def __init__(self,initial_agent_loc,N,monster_coords,food_coords):
        self.initial_agent_loc = initial_agent_loc
        self.N = N
        self.monster_coords = monster_coords
        self.food_coords = food_coords
        tmp = [0]+[False for i in food_coords]
        self.initial_state = initial_agent_loc + tuple(tmp)
    def actions(self,state):
        l = []
        if state[2] == 0: #init up
            if (state[0],state[1]+1) in [(i[0],i[1]) for i in self.monster_coords]:
                l.append('up')
        elif state[2] == 1: #left left
            if (state[0]-1,state[1]) in [(i[0]-1,i[1]) for i in self.monster_coords]:
                l.append('left')
        elif state[2] == 2: #init down
            if (state[0],state[1]-1) in [(i[0],i[1]) for i in self.monster_coords]:
                l.append('down')
        elif state[2] == 3: #right
            if (state[0]+1,state[1]) in [(i[0]+1,i[1]) for i in self.monster_coords]:
                l.append('right')
        return l
    def result(self,state,action):
        match action:
            case 'right':
                state[0]+=1
            case 'left':
                state[0]-=1
            case 'up':
                state[1]+=1
            case 'down':
                state[1]-=1
        state[2] = (1 + state[2]) % 4
        if tuple(state[0,1]) in self.food_coords:
            f = self.food_coords.index(action)
            state[f] = True
        return state
    def action_cost(state1,action,state2):
        return 1
    def is_goal(self,state):
        return all(state[3:])
    def h (self,node):
        if self.is_goal(self.initial_state):
            return 0
        l = []
        for i in self.food_coords:
            l.append(abs(node[1]-i[1])+abs(node[0]-i[0]))
        return min(l)




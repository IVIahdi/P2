class ConstrainedRouteProblem:
    def __init__(self, initial_agent_loc, goal_loc, map_edges, map_coords, must_visit):
        self.initial_agent_loc = initial_agent_loc
        self.goal_loc = goal_loc
        self.map_edges = map_edges
        self.map_coords = map_coords
        self.must_visit = must_visit
        temp = [False for i in must_visit]
        self.initial_state = (initial_agent_loc, False, False) + tuple(temp)
    def actions(self, state):
        temp = [i for i in self.map_edges.keys() if state[0] in i]
        temp2 = []
        for i in temp:
            if state[0] == i[0]:
                temp2.append(i[1])
            if state[0] == i[1]:
                temp2.append(i[0])
        return temp2
    def result(self, state, action):
        s = list(state)
        s[0] = action
        if action == self.goal_loc and s[1] == True:
            s[2] = True
        if action == self.goal_loc:
            s[1] = True
        if action in self.must_visit:
            s[self.must_visit.index(action) + 3] = True
        return tuple(s)
    def action_cost(self,state1, action, state2):
        try:
            return self.map_edges[state2[0], state1[0]]
        except:
            return self.map_edges[state1[0], state2[0]]
    def is_goal(self,state):
        return state[0] == self.goal_loc and all(state[3:]) and state[1] and not state[2]
    def h(self,node):
        if node == self.goal_loc:
            return 0
        x = (((self.map_coords[node.state[0]][0]-self.map_coords[self.goal_loc][0])) ** 2 + ((self.map_coords[node.state[0]][1]-self.map_coords[self.goal_loc][1]))**2)**0.5
        return x
class GridProblemWithMonsters:
    def __init__(self,initial_agent_loc,N,monster_coords,food_coords):
        self.initial_agent_loc = initial_agent_loc
        self.N = N
        self.monster_coords = monster_coords
        self.food_coords = food_coords
        tmp = [0]+[False for i in food_coords]
        self.initial_state = (initial_agent_loc) + tuple(tmp)
    def actions(self,state):
        s = list(state)
        print(s)
        print(self.monster_coords)
        actions = []
        upA = s[0]+1,s[1]
        downA = s[0]-1,s[1]
        rightA = s[0],s[1]+1
        leftA = s[0],s[1]-1

        mosLoc = self.monster_coords
        mstep = (s[2] + 1 ) % 4
        match(mstep):
            case 1:
                mosLoc = [(i[0],i[1]-1) for i in mosLoc]
            case 3:
                mosLoc = [(i[0],i[1]+1) for i in mosLoc]
        if upA not in mosLoc and all(upA) <= self.N:
            actions.append('up')
        if downA not in mosLoc and all(downA) <= self.N:
            actions.append('down')
        if rightA not in mosLoc and all(rightA) <= self.N:
            actions.append('right')
        if leftA not in mosLoc and all(leftA) <= self.N:
            actions.append('left')
        return actions
    def result(self,state,action):
        s = list(state)
        s[2] = ((s[2] + 1) % 4)
        match(action):
            case 'left':
                s[1] -=1
            case 'right':
                s[1] +=1
            case 'up':
                s[0] +=1
            case 'down':
                s[0] -=1
        x = tuple([s[0],s[1]])
        if x in self.food_coords:
            s[self.food_coords.index(x) + 3] = True
        return tuple(s)
    def action_cost(self,state1,action,state2):
        return 1
    def is_goal(self,state):
        return all(state[3:])
    def h (self,node):
        loc = tuple(node.state[:2])
        if self.is_goal(node.state):
            return 0
        xx = [i for i in self.food_coords if node.state[self.food_coords.index(i) + 3] == False]
        x = []
        for i in xx:
            d = ((i[0]-loc[0])**2 + (i[1]-loc[1])**2)**0.5
            x.append(d)
        return min(x)
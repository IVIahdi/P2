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
        tmp = [False for i in food_coords]
        self.initial_state = (initial_agent_loc,0) + tuple(tmp)
    def actions(self,state):
        l = ['left','right','up','down']
        print(state,1231654165)
        if state[2] == 0:
            up = tuple([state[0]+1,state[1]])
            if up in self.monster_coords or any(up) > self.N:
                l.remove('up')
            down = tuple([state[0]-1,state[1]])
            if down in self.monster_coords or any(down) > self.N:
                l.remove('down')
            left = tuple([state[0],state[1]-1])
            if left in self.monster_coords or any(left) > self.N:
                l.remove('left')
            right = tuple([state[0],state[1]+1])
            if right in self.monster_coords or any(right) > self.N:
                l.remove('right')
        elif state[2] == 1:
            up = tuple([state[0]+1,state[1]])
            if up in ((i[0],i[1]-1) for i in self.monster_coords) or any(up) > self.N:
                l.remove('up')
            down = tuple([state[0]-1,state[1]])
            if down in ((i[0],i[1]-1) for i in self.monster_coords) or any(down) > self.N:
                l.remove('down')
            left = tuple([state[0],state[1]-1])
            if left in ((i[0],i[1]-1) for i in self.monster_coords) or any(left) > self.N:
                l.remove('left')
            right = tuple([state[0],state[1]+1])
            if right in ((i[0],i[1]-1) for i in self.monster_coords) or any(right) > self.N:
                l.remove('right')
        elif state[2] == 2:
            up = tuple([state[0]+1,state[1]])
            if up in self.monster_coords or any(up) > self.N:
                l.remove('up')
            down = tuple([state[0]-1,state[1]])
            if down in self.monster_coords or any(down) > self.N:
                l.remove('down')
            left = tuple([state[0],state[1]-1])
            if left in self.monster_coords or any(left) > self.N:
                l.remove('left')
            right = tuple([state[0],state[1]+1])
            if right in self.monster_coords or any(right) > self.N:
                l.remove('right')
        elif state[2] == 3:
            up = tuple([state[0]+1,state[1]])
            if up in ((i[0],i[1]+1) for i in self.monster_coords) or any(up) > self.N:
                l.remove('up')
            down = tuple(state[0][0]-1,state[0][1])
            if down in ((i[0],i[1]+1) for i in self.monster_coords) or any(down) > self.N:
                l.remove('down')
            left = tuple([state[0],state[1]-1])
            if left in ((i[0],i[1]+1) for i in self.monster_coords) or any(left) > self.N:
                l.remove('left')
            right = tuple([state[0],state[1]+1])
            if right in ((i[0],i[1]+1) for i in self.monster_coords) or any(right) > self.N:
                l.remove('right')
        return l
    def result(self,state,action):
        state = list(state)
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
        if tuple(state[0:2]) in self.food_coords:
            f = self.food_coords.index(action)
            state[f] = True
        return state
    def action_cost(self,state1,action,state2):
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




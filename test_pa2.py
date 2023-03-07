from problem import *
from search_algorithms import *
from collections import Counter

class CallCounter:
    def __init__(self, obj):
        self.object = obj # the object being wrapped, for this assignment, it will be a Problem object
        self.counter = Counter() # the count dictionary for function calls
        
    def __getattr__(self, attr):
        self.counter[attr] += 1 # everytime function attr is called, increment the counter for it
        return getattr(self.object, attr) # then call the function 


def print_stat_report(searchers, problems, searcher_names=None):
    for i, searcher in enumerate(searchers):
        sname = searcher.__name__
        if searcher_names is not None:
            sname = searcher_names[i]
        print(sname)
        total_counts = Counter()
        for p in problems:
            prob   = CallCounter(p) # wrap the problem object in the counter
            soln   = searcher(prob) # run search algorithm
            counter = prob.counter;  # get the counter dict
            
            # get solution cost
            if soln is None:        
                counter.update(solndepth=0, solncost=0)
            else:
                counter.update(solndepth=soln.depth, solncost=soln.path_cost)
                
            # maintain total for the current search algorithm
            total_counts += counter
            print_counts_helper(counter, str(p)[:30])
        print_counts_helper(total_counts, 'TOTAL\n')
        print('----------------------------------------------------------------')
        
def print_counts_helper(counter, name):
    print('{:9,d} generated nodes |{:9,d} popped |{:5.0f} solution cost |{:8,d} solution depth | {}'.format(
          counter['result'], counter['is_goal'], counter['solncost'], counter['solndepth'], name))

if __name__ == "__main__":
    # constrained route problem example
    example_map_edges = { ('R', 'D'): 410,
                        ('R', 'H'): 620,
                        ('R', 'J'): 950,
                        ('R', 'A'): 950,
                        ('D', 'B'): 110,
                        ('H', 'B'): 940,
                        ('H', 'T'): 680,
                        ('B', 'T'): 1600,
                        ('J', 'A'): 680,
                        ('J', 'Y'): 330,
                        ('Y', 'T'): 680
                        }

    example_coords = {'A': (0,200),
                      'B': (1250,600), 
                      'D': (1300,550),
                      'H': (500,850),
                      'J': (100,450),
                      'T': (0,1300),
                      'R': (950,500),
                      'Y': (50,750)
                      }

    example_must_visit = ['R', 'H', 'T', 'Y']


    example_route_problem = ConstrainedRouteProblem(initial_agent_loc='D', goal_loc='J', 
                                                     map_edges=example_map_edges, 
                                                     map_coords=example_coords, 
                                                     must_visit =example_must_visit)

    example_state = ('R', False, False, True, False, False, False)
    print('For ConstrainedRouteProblem. From state: {}. we have the following actions available:'.format(example_state))
    actions_available = example_route_problem.actions(state=example_state)
    print(actions_available)
    print('------------------------------------------------------------------')
    
    # grid problem with monsters example
    example_monster_coords = [(5,2), (3,3), (1,2)] 

    example_food_coords = [(5,4), (3,2), (1,3)]

    example_grid_problem = GridProblemWithMonsters(initial_agent_loc=(4,5), 
                                                    N=5, 
                                                    monster_coords=example_monster_coords,
                                                    food_coords=example_food_coords)
    
    example_state = (1, 2, 1, True, True, False)
    print('For GridProblemWithMonsters. From state: {}. we have the following actions available:'.format(example_state))
    actions_available = example_grid_problem.actions(state=example_state)
    print(actions_available)
    print('------------------------------------------------------------------')
    
    # get some statistics on generated nodes, popped nodes, solution
    searchers1 = [breadth_first_search, depth_first_search, uniform_cost_search]
    problems = [example_route_problem, example_grid_problem]
    print_stat_report(searchers1, problems, searcher_names=['BFS', 'DFS', 'UCS'])
    
    # note: to use print_stat_report with search algorithms that take in more than the problem argument, 
    # you need to wrap the search algorithm in a wrapper.
    # for example, to use astar treelike version on a route problem p, you can define the following wrapper.
    def astar_treelike_wrapper(p):
        return astar_search(p, h=p.h, treelike=True)
        
    # Or a convenient alternative is to define lambda function (lambda p: greedy_search(p, h=p.h_euclidean, treelike=True))
    searchers2 = [astar_treelike_wrapper, (lambda p: astar_search(p, h=p.h)), (lambda p: greedy_search(p, h=p.h, treelike=False))]
    print_stat_report(searchers2, problems, searcher_names=['astar_treelike', 'astar', 'greedy'])
    
    # add your own problems and try printing report. 
    goal_node = breadth_first_search(example_route_problem)
    print('printing solution path')
    print(get_path_states(goal_node))
    print('printing solution-actions-path')
    print(get_path_actions(goal_node))
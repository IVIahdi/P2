if __name__ == "__main__":
    from problem import *
    from search_algorithms import *

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

    goal_node = breadth_first_search(example_route_problem)
    visualize_route_problem_solution(example_route_problem, goal_node, './route.png')    
    plt.close()
    
    # grid problem with monsters example
    example_monster_coords = [(5,2), (3,3), (1,2)] 

    example_food_coords = [(5,4), (3,2), (1,3)]

    example_grid_problem = GridProblemWithMonsters(initial_agent_loc=(4,5), 
                                                    N=5, 
                                                    monster_coords=example_monster_coords,
                                                    food_coords=example_food_coords)

    goal_node = breadth_first_search(example_grid_problem)
    visualize_grid_problem_solution(example_grid_problem, goal_node, './grid.png')
    plt.close()
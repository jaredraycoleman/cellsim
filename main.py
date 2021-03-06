from cellsim import System, States
import math
import random


def get_new_state(state, mutation_prob, red_neighbors, blue_neighbors, green_neighbors, yellow_neighbors):
    
    n = sum([red_neighbors, blue_neighbors, green_neighbors])
    if state == States.RED:
        
        if n <= 2 or blue_neighbors > math.ceil(n / 2):
            return States.BLUE
        else:
            if random.random() < mutation_prob:
                return States.YELLOW
            return States.RED
    elif state == States.BLUE:
        if red_neighbors > math.floor(n / 2):
            return States.RED
        else:
            return States.BLUE
    elif state == States.YELLOW:
        if n < 3 or red_neighbors == 0:
            return States.BLUE
        elif red_neighbors > 2 * n / 3:
            return States.RED
        else:
            return States.YELLOW

    print(state)

if __name__ == '__main__':
    system = System(size=1000,
                    radius=0.05, 
                    red_freq=0.7, 
                    blue_freq=0.3,
                    green_freq=0.0,
                    yellow_freq=0.0,
                    mutation_prob=0.01,
                    get_new_state=get_new_state)
    system.start()
from cellsim import System, States
import math

def get_new_state(state, red_neighbors, blue_neighbors, green_neighbors):
    n = sum([red_neighbors, blue_neighbors, green_neighbors])
    if state == States.RED:
        if n <= 2 or red_neighbors < math.ceil(n/4):
            return States.BLUE
        elif red_neighbors >= math.ceil(n/4):
            return States.RED
    elif state == States.BLUE:
        if red_neighbors > math.floor(3 * n / 8):
            return States.RED
        else:
            return States.BLUE
    elif state == States.GREEN:
        if n < 3 or blue_neighbors > 2 * n / 3:
            return States.RED
        else:
            return States.GREEN

if __name__ == '__main__':
    system = System(size=1000,
                    radius=0.025, 
                    red_freq=0.7, 
                    blue_freq=0.29,
                    green_freq=0.01,
                    mutation_prob=0.001,
                    get_new_state=get_new_state)
    system.start()
import os 
import sys
import numpy as np
import scipy.spatial as spatial
import random

import matplotlib.pyplot as plt
import matplotlib.animation as animation

init = {
    'n_robots': 1000,
    'rounds': None,
    'radius': 0.05,
    'states': {
        0: 0.6,
        1: 0.25,
        2: 0.15
    },
    'mutation': 0.05
}

colors = {
    0: 'red',
    1: 'blue', 
    2: 'green'
}

def get_new_state(state, neighbor_states):
    if random.random() < init['mutation']:
        return 2
    if state == 0:
        if neighbor_states.size < 2:
            return 1
        if neighbor_states[0] > 0.2:
            return 0
        if neighbor_states[1] > 0.7:
            return 1 
        return 0
    elif state == 1:
        if neighbor_states.size < 2:
            return 1
        if neighbor_states[0] > 0.2:
            return 0
        return 1
    elif state == 2:
        if (neighbor_states.size < 3 or neighbor_states[1] > 0.5):
            return 1
        return 2 

if __name__ == '__main__':
    size = init['n_robots']
    radius = init['radius']

    probs = [init['states'][state] for state in sorted(init['states'].keys())]
    states = np.random.choice([0, 1, 2], size=size, p=probs)

    points = np.random.random((size, 2))
    point_tree = spatial.cKDTree(points)

    fig, ax = plt.subplots()

    x, y = zip(*points)
    g_points = []
    for (i,) in np.ndindex(points.shape[:1]):
        x = points[i][0]
        y = points[i][1]
        plot, = ax.plot(x, y, 'o', c=colors[states[i]])
        g_points.append(plot)
    
    def animate(i):
        global points, point_tree     
        for (i,) in np.ndindex(points.shape[:1]):
            x = points[i][0]
            y = points[i][1]
            _, neighbor_states = np.unique([states[j] for j in point_tree.query_ball_point([x, y], radius)], return_counts=True)

            if neighbor_states.size > 0:
                neighbor_states = np.divide(neighbor_states, sum(neighbor_states))

            states[i] = get_new_state(states[i], neighbor_states)
            g_points[i].set_color(colors[states[i]])

            direction = np.multiply(np.random.random(2) - 0.5, radius)
            points[i] = np.add(points[i], direction)
        point_tree = spatial.cKDTree(points)

    ax.axis([-0.2,1.2,-0.2,1.2])
    ani = animation.FuncAnimation(fig, animate, interval=100)
    plt.show()
        
        

import os 
import sys
import numpy as np
import scipy.spatial as spatial
import random
import math

import matplotlib.pyplot as plt
import matplotlib.animation as animation

class States:
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3

class System:
    def __init__(self, size, radius, mutation_prob, get_new_state, 
                 red_freq = 0.5,
                 blue_freq = 0.5, 
                 green_freq=0.0, 
                 yellow_freq=0.0): 
        self.state_freq = {
            States.RED: red_freq,
            States.BLUE: blue_freq,
            States.GREEN: green_freq,
            States.YELLOW: yellow_freq,
        }
        
        self.state_colors = {
            States.RED: 'red',
            States.BLUE: 'blue',
            States.GREEN: 'green',
            States.YELLOW: 'yellow',
        }

        self.size = size
        self.radius = radius
        self.mutation_prob = mutation_prob

        self.get_new_state = get_new_state
        self.n_states = len(self.state_freq.keys())
        probs = [self.state_freq[state] for state in sorted(self.state_freq.keys())]
        self.states = np.random.choice([States.RED, States.GREEN, States.BLUE, States.YELLOW], size=self.size, p=probs)

        self.points = np.random.random((self.size, 2))
        self.point_tree = spatial.cKDTree(self.points)

        self.fig, ax = plt.subplots()

        x, y = zip(*self.points)
        self.g_points = []
        for (i,) in np.ndindex(self.points.shape[:1]):
            x = self.points[i][0]
            y = self.points[i][1]
            plot, = ax.plot(x, y, 'o', c=self.state_colors[self.states[i]])
            self.g_points.append(plot)

        ax.axis([-0.2,1.2,-0.2,1.2])

    def state_machine(self, state, neighbor_states):
        #if random.random() < self.mutation_prob:
        #    return 2

        new_state = self.get_new_state(state, self.mutation_prob, *neighbor_states)

        if new_state is None:
            raise Exception('Invalid state')

        return new_state

    def start(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=100)
        plt.show()

    def animate(self, i):
        new_states = np.zeros(self.size, dtype=int)
        for (i,) in np.ndindex(self.points.shape[:1]):
            state_counts = np.zeros(self.n_states) 
            x = self.points[i][0]
            y = self.points[i][1]
            for j in self.point_tree.query_ball_point([x, y], self.radius):
                state_counts[self.states[j]] += 1

            if self.states[i] % 2 != 0:
                direction = np.multiply(np.random.random(2) - 0.5, self.radius)
                self.points[i] = np.add(self.points[i], direction)
                self.g_points[i].set_data(self.points[i][0], self.points[i][1])

            # Uncomment for asynchrnous (kind of)
            self.states[i] = self.state_machine(self.states[i], state_counts)
            self.g_points[i].set_color(self.state_colors[self.states[i]])

        # # Uncomment for synchronous
        #     new_states[i] = self.state_machine(self.states[i], state_counts) 
        # self.states = new_states 
        # for i in range(self.size):
        #     self.g_points[i].set_color(self.state_colors[self.states[i]])

        self.point_tree = spatial.cKDTree(self.points)


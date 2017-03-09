from vector import vector
from cluster import cluster
import numpy as np
from color import color
from energy import energy
from status import status


class entity:

    def __init__(self, point, color):
        self.point = point
        self.color = color
        self.cluster = cluster(self)
        self.status = status(np.random.randint(2), 10, 10)
        self.energy = energy(1, np.random.randn(), np.random.randn(7) - 3)

    @property
    def state(self):
        return self.status.state

    @state.setter
    def state(self, value):
        self.status.state = value

    def tick(self):
        self.cluster.seek()
        self.state_to_color()

    def force(self, force):
        self.point.acc += force / self.energy.mass

    def seek(self, target):
        desired = vector.maxout(target - np.array(self.point.pos), self.status.max_speed)
        force = vector.limit(desired - self.point.vel, self.status.max_force)
        self.force(np.sum(force, axis=0))
        # desired = vector.maxout(target - self.point.pos, self.status.max_speed)
        # self.force(vector.limit(desired - self.point.vel, self.status.max_force))

    def avoid(self, target):
        desired = vector.maxout(target - self.point.pos, self.status.max_speed)
        self.force(-vector.limit(desired - self.point.vel, self.status.max_force))

    def state_to_color(self):
        if self.state == 0:
            self.color = color.random_hue(120, 240)
            self.state = 1
        elif self.state == 1:
            self.color = color.random_hue(240, 360)
            self.state = 0
        elif self.state == 2:
            self.color = color.random_hue(0, 120)

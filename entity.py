from vector import vector
from cluster import cluster
import numpy as np


class entity:

    def __init__(self, point, color):
        self.point = point
        self.color = color
        self.cluster = cluster(self)
        self.state = np.random.randint(3)
        # self.state_to_color()

    def tick(self):
        self.cluster.break_bond(100)
        self.cluster.seek()
        # self.state_tick()

    def seek(self, target):
        desired = vector.maxout(target - self.point.pos, 6)
        self.point.force(vector.limit(desired - self.point.vel, 6))

    def avoid(self, target):
        desired = vector.maxout(target - self.point.pos, 6)
        self.point.force(-vector.limit(desired - self.point.vel, 6))

    def state_tick(self):
        for ent in self.cluster.ents:
            if ent.state != self.state:
                self.seek(ent.point.pos)
                self.color = np.array([0, 255, 0])
            else:
                self.avoid(ent.point.pos)
                self.color = np.array([255, 0, 0])

    def state_to_color(self):
        if self.state == 0:
            self.color = np.array([255, 0, 0])
        if self.state == 1:
            self.color = np.array([0, 255, 0])
        if self.state == 2:
            self.color = np.array([0, 0, 255])

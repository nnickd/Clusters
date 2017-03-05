from vector import vector
from cluster import cluster
import numpy as np
from color import color


class entity:

    def __init__(self, point, color):
        self.point = point
        self.color = color
        self.cluster = cluster(self)
        self.state = np.random.randint(2)

    def tick(self):
        self.cluster.break_bond(100)
        self.cluster.seek()
        self.state_to_color()

    def seek(self, target):
        desired = vector.maxout(target - self.point.pos, 6)
        self.point.force(vector.limit(desired - self.point.vel, 6))

    def avoid(self, target):
        desired = vector.maxout(target - self.point.pos, 6)
        self.point.force(-vector.limit(desired - self.point.vel, 6))

    def state_to_color(self):
        if self.state == 0:
            self.color = color.random_hue(120, 240)
            self.state = 1
        elif self.state == 1:
            self.color = color.random_hue(240, 360)
            self.state = 0
        elif self.state == 2:
            self.color = color.random_hue(0, 120)

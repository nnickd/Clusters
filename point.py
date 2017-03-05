from vector import vector
import numpy as np


class point:

    def __init__(self, pos=np.array([0., 0.]), vel=np.array([0., 0.]), acc=np.array([0., 0.])):
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def lerp(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def force(self, force):
        self.acc += force

    def bound(self, pos, dist):
        if vector.magnitude(self.pos - pos) > dist:
            self.vel *= -1

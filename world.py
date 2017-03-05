import numpy as np
from point import point
from entity import entity


class world:

    def __init__(self, cluster):
        self.cluster = cluster

    def tick(self):
        self.cluster.bond(100)
        for ent in self.cluster.ents:
            ent.tick()
        for ent in self.cluster.ents:
            ent.point.lerp()
            ent.point.bound(np.array([960., 540.]), 540)

    @property
    def amount(self):
        return len(self.cluster.ents)

    @property
    def vertices(self):
        return np.array([ent.point.pos for ent in self.cluster.ents]).ravel()

    @property
    def colors(self):
        return np.array([ent.color for ent in self.cluster.ents]).ravel()

    def add_to_coord(self, x, y):
        pt = point(np.array([x, y], dtype='f'), np.array([0., 0.]), np.array([0., 0.]))
        ent = entity(pt, np.array([0., 255., 0.]))
        self.cluster.add(ent)

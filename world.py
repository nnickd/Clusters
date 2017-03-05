import numpy as np
from point import point
from vector import vector
from entity import entity


class world:

    def __init__(self, cluster):
        self.cluster = cluster
        self.verts = point()

    def tick(self):
        self.cluster.bond(100)
        for ent in self.cluster.ents:
            ent.tick()
        for ent in self.cluster.ents:
            ent.point.lerp()
            ent.point.bound(np.array([960., 540.]), 400)

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
        pos = np.array([x, y], dtype='f')
        pt = point(pos, np.array([0., 0.]), np.array([0., 0.]))
        ent = entity(pt, np.array([0, 0, 255]))
        self.cluster.add(ent)

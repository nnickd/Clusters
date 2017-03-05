import numpy as np
from point import point
from entity import entity
from color import color
from cluster import cluster
from vector import vector


class world:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.origin = np.array([self.width/2, self.height/2])
        self.root = entity(point(self.origin, np.array([0., 0.]), np.array([0., 0.])), np.array([0., 0., 0.]))
        self.cluster = cluster(self.root)

    def tick(self):
        self.cluster.bond(100)
        for ent in self.cluster.ents:
            ent.tick()
        for ent in self.cluster.ents:
            ent.point.lerp()
            ent.point.bound(self.origin, 540)

    def create(self, amount):
        e = []
        for i in range(amount):
            p = point(vector.random(self.origin, 300), np.array([0., 0.]), np.array([0., 0.]))
            c = color.random_hue(0, 360)
            ent = entity(p, c)
            e.append(ent)
        self.cluster.add(*e)

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

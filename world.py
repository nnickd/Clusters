import numpy as np


class world:

    def __init__(self, cluster):
        self.entities = cluster

    def tick(self):
        for ent in self.entities.ents:
            ent.tick()
        for ent in self.entities.ents:
            ent.point.lerp()

    @property
    def amount(self):
        return len(self.entities.ents)

    @property
    def vertices(self):
        return np.array([ent.point.pos for ent in self.entities.ents]).ravel()

    @property
    def colors(self):
        return np.array([ent.color for ent in self.entities.ents]).ravel()

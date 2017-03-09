from vector import vector
import numpy as np


class cluster:

    def __init__(self, entity):
        self.ent = entity
        self.ents = []

    @property
    def pos(self):
        return np.array([ent.point.pos for ent in self.ents])

    def add(self, *ents):
        for ent in ents:
            self.ents.append(ent)

    def remove(self, *ents):
        if len(self.pos) > 0:
            self.ent.avoid(self.pos)

    def seek(self):
        if len(self.pos) > 0:
            self.ent.seek(self.pos)

    def avoid(self):
        for ent in self.ents:
            self.ent.avoid(ent.point.pos)

    def bond(self, distance):
        for i in range(len(self.ents)):
            for j in range(len(self.ents) - i):
                x, y = self.ents[i], self.ents[j + i]
                dist = vector.distance(x.point.pos, y.point.pos)
                if dist < distance and dist > 0 and y not in x.cluster.ents:
                    x.cluster.add(y)
                    y.cluster.add(x)
                    if dist >= distance and y in x.cluster.ents:
                        x.cluster.remove(y)
                        y.cluster.remove(x)
        # for entx in self.ents:
        #     for enty in self.ents:
        #         dist = vector.distance(entx.point.pos, enty.point.pos)
        #         if dist < distance and dist > 0 and enty not in entx.cluster.ents:
        #             entx.cluster.add(enty)
        #         if dist >= distance and enty in entx.cluster.ents:
        #             entx.cluster.remove(enty)

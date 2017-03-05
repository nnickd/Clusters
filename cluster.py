from vector import vector


class cluster:

    def __init__(self, entity):
        self.ent = entity
        self.ents = []

    def add(self, *ents):
        for ent in ents:
            self.ents.append(ent)

    def remove(self, *ents):
        for ent in ents:
            self.ents.remove(ent)

    def seek(self):
        for ent in self.ents:
            self.ent.seek(ent.point.pos)

    def avoid(self):
        for ent in self.ents:
            self.ent.avoid(ent.point.pos)

    def break_bond(self, distance):
        for ent in self.ents:
            if vector.distance(self.ent.point.pos, ent.point.pos) >= distance:
                self.remove(ent)

    def bond(self, distance):
        for entx in self.ents:
            for enty in self.ents:
                dist = vector.distance(entx.point.pos, enty.point.pos)
                if dist < distance and dist > 0 and enty not in entx.cluster.ents:
                    entx.cluster.add(enty)

from vector import vector
from cluster import cluster


class entity:

    def __init__(self, point, color):
        self.point = point
        self.color = color
        self.cluster = cluster()

    def tick(self):
        self.seek_cluster()

    def seek(self, target):
        desired = vector.maxout(target - self.point.pos, 100)
        self.point.force(vector.limit(desired - self.point.vel, 100))

    def seek_cluster(self):
        for ent in self.cluster.ents:
            self.seek(ent.point.pos)

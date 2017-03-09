import numpy as np
import colorsys


class tree:

    def __init__(self, amount):
        self.amount = amount
        self.color = np.zeros((amount, 3))
        self.pos = np.zeros((amount, 2))
        # self.colors = np.array([])

        self.vel = np.zeros((amount, 2))
        self.acc = np.zeros((amount, 2))
        self.ids = np.arange(amount)
        self.bonds = []

    @property
    def vertices(self):
        return self.pos.ravel()

    @property
    def colors(self):
        return self.color.ravel()

    def add_bond(self, a, b):
        self.bonds.append((a, b))

    def remove_bond(self, a, b):
        if (a, b) in self.bonds:
            self.bonds.remove((a, b))

    def add_point(self, pos, vel, acc, hue):
        self.pos = np.append(self.pos, pos)
        self.vel = np.append(self.vel, vel)
        self.acc = np.append(self.acc, acc)
        self.add_color(140)
        self.amount += 1
        self.ids = np.arange(self.amount)

    def remove_point(self, index):
        np.delete(self.pos, index, 0)
        np.delete(self.vel, index, 0)
        np.delete(self.acc, index, 0)
        self.remove_color(index)
        self.amount -= 1
        self.ids = np.arange(self.amount)

    def add_color(self, hue):
        color = np.array(colorsys.hsv_to_rgb(hue / 360, 1, 1)) * 255
        self.color = np.append(self.color, color)

    def remove_color(self, index):
        np.delete(self.color, index, 0)

    def tick(self):
        self.proximity_bond(100)
        self.cluster_seek(10)
        self.lerp()

    def lerp(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def force(self, index, force):
        self.acc[index] += force

    def seek(self, index, target, limit):
        desired = target - self.pos[index]
        desired = np.linalg.norm(desired) * limit
        force = desired - self.vel[index]
        if np.linalg.norm(force) > limit:
            force = np.linalg.norm(force) * limit
        self.force(index, force)

    def cluster_seek(self, limit):
        for bond in self.bonds:
            self.seek(bond[0], self.pos[bond[1]], limit)
            self.seek(bond[1], self.pos[bond[0]], limit)

    def proximity_bond(self, distance):
        for i in self.ids:
            for j in self.ids + i:
                radius = np.linalg.norm(self.pos[i] - self.pos[j])
                if radius < distance:
                    self.add_bond(i, j)
                if radius > distance:
                    self.remove_bond(i, j)

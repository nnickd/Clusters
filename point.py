from vector import vector


class point:

    def __init__(self, pos, vel, acc):
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

    @property
    def speed(self):
        return vector.magnitude(self.vel)

    @property
    def direction(self):
        return vector.angle(self.vel, vector.make(1, 0))

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

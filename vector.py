import numpy as np


class vector:

    def magnitude(vec):
        return np.linalg.norm(vec)

    def normalize(vec):
        return vec / np.linalg.norm(vec)

    def maxout(vec, lim):
        return vector.normalize(vec) * lim

    def limit(vec, lim):
        if np.linalg.norm(vec) > lim:
            vec = vector.maxout(vec, lim)
        return vec

    def distance(vec1, vec2):
        return np.linalg.norm(vec1 - vec2)

    def angle(vec1, vec2):
        return np.arccos(np.clip(np.dot(vector.normalize(vec1), vector.normalize(vec2)), -1.0, 1.0))

    def make(x, y):
        return np.array([x, y])

    def random(origin, radius):
        theta = np.random.rand() * 360
        return vector.rotate(theta) @ np.array([1, 0]) * np.random.rand() * radius + origin

    def rotate(theta):
        rad = np.radians(theta)
        c, s = np.cos(rad), np.sin(rad)
        return np.array([[c, -s], [s, c]])

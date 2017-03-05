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

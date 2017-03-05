import numpy as np


class vector:

    def normalize(vec):
        return vec / np.linalg.norm(vec)

    def maxout(vec, lim):
        return vector.normalize(vec) * lim

    def limit(vec, lim):
        if np.linalg.norm(vec) > lim:
            vec = vector.maxout(vec, lim)
        return vec

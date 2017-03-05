from render import render
from world import world
from entity import entity
import numpy as np
from cluster import cluster
from point import point
from vector import vector

width, height = 1920, 1080
origin = np.array([width // 2, height // 2])

e = []

for i in range(30):
    pos = vector.random(origin, 100)
    p = point(pos, np.array([0., 0.]), np.array([0., 0.]))
    c = np.array([0, 255, 0])
    ent = entity(p, c)
    e.append(ent)

ent = entity(point(np.array([960., 540.]), np.array([0., 0.]), np.array([0., 0.])), np.array([0., 0., 0.]))

cluster = cluster(ent)
cluster.add(*e)

world = world(cluster)
render(world)

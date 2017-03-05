from render import render
from world import world
from entity import entity
import numpy as np
from cluster import cluster
from point import point

width, height = 1920, 1080

e = []

for i in range(6):
    pos = np.random.randn(2) * (np.random.rand() * 100) + np.array([width/2, height/2])
    p = point(pos, np.array([0., 0.]), np.array([0., 0.]))
    c = np.array([0, 255, 0])
    ent = entity(p, c)
    e.append(ent)

e[0].cluster.add(e[1])
e[1].cluster.add(e[2], e[3])
e[2].cluster.add(e[3], e[4], e[5])
e[3].cluster.add(e[4], e[5], e[0], e[1])
e[4].cluster.add(e[5])
e[5].cluster.add(e[0])

cluster = cluster()
cluster.add(*e)

world = world(cluster)
render(world)

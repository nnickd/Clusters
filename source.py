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

ent = entity(point(np.array([960., 540.]), np.array([0., 0.]), np.array([0., 0.])), np.array([0, 0, 0]))

cluster = cluster(ent)
cluster.add(*e)

world = world(cluster)
render(world)

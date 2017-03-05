from render import render
from world import world


world = world(1920, 1080)
world.create(30)
render(world)

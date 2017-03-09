import pyglet
from pyglet.window import mouse, key
from tree import tree
import numpy as np


class seed(object):
    window = pyglet.window.Window(fullscreen=True)
    batch = pyglet.graphics.Batch()
    vertex_list = None
    tree = None
    clear = True
    pause = False
    chosen = None

    def __init__(self, amount):
        seed.tree = tree(amount)
        seed.vertex_list = seed.batch.add(seed.tree.amount, pyglet.gl.GL_POINTS, None, ('v2f', seed.tree.vertices), ('c3f', seed.tree.colors))
        pyglet.clock.schedule_interval(self.update, 1/30)
        pyglet.app.run()

    def update(self, dt):
        seed.vertex_list.resize(seed.tree.amount)
        if not seed.pause:
            seed.tree.tick()
        seed.vertex_list.vertices = seed.tree.vertices
        seed.vertex_list.colors = seed.tree.colors

    @window.event
    def on_draw():
        if seed.clear:
            seed.window.clear()
        seed.batch.draw()

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.DOWN:
            seed.clear = not seed.clear
        if symbol == key.UP:
            seed.pause = not seed.pause

    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            seed.tree.add_point(np.array([x, y]), np.array([0., 0.]), np.array([0., 0.]), 140)
        if buttons & mouse.RIGHT:
            if seed.tree.amount > 1:
                seed.tree.remove_point(0)

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            pass
        if button == mouse.RIGHT:
            pass

import pyglet
from pyglet.window import mouse, key
import numpy as np
from vector import vector


class render(object):
    window = pyglet.window.Window(fullscreen=True)
    batch = pyglet.graphics.Batch()
    vertex_list = None
    world = None
    clear = True
    pause = False
    chosen = None

    def __init__(self, world):
        render.world = world
        render.chosen = render.world.cluster.ents[0]
        render.vertex_list = render.batch.add(world.amount, pyglet.gl.GL_POINTS, None, ('v2f', world.vertices), ('c3f', world.colors))
        pyglet.clock.schedule_interval(self.update, 1/30)
        pyglet.app.run()

    def update(self, dt):
        render.vertex_list.resize(render.world.amount)
        if not render.pause:
            render.world.tick()
        render.vertex_list.vertices = render.world.vertices
        render.vertex_list.colors = render.world.colors

    @window.event
    def on_draw():
        if render.clear:
            render.window.clear()
        render.batch.draw()

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.DOWN:
            render.clear = not render.clear
        if symbol == key.UP:
            render.pause = not render.pause

    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            if render.world.amount > 60:
                del render.world.cluster.ents[0]
            render.world.add_to_coord(x, y)
        if buttons & mouse.RIGHT:
            if render.world.amount > 1:
                del render.world.cluster.ents[0]
                render.chosen

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            if render.world.amount > 69:
                del render.world.cluster.ents[0]
            render.world.add_to_coord(x, y)
        if button == mouse.RIGHT:
            render.chosen.state = 1
            e = render.world.cluster.ents[0]
            mouse_xy = np.array([x, y])
            for ent in render.world.cluster.ents:
                if vector.distance(ent.point.pos, mouse_xy) < vector.distance(e.point.pos, mouse_xy):
                    e = ent
            e.state = 2
            render.chosen = e

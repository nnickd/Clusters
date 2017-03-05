import pyglet
from pyglet.window import mouse, key


class render(object):
    window = pyglet.window.Window(fullscreen=True)
    batch = pyglet.graphics.Batch()
    vertex_list = None
    world = None

    def __init__(self, world):
        render.world = world
        render.vertex_list = render.batch.add(world.amount, pyglet.gl.GL_POINTS, None, ('v2f', world.vertices), ('c3B', world.colors))
        pyglet.clock.schedule_interval(self.update, 1/30)
        pyglet.app.run()

    def update(self, dt):
        render.vertex_list.resize(render.world.amount)
        render.world.tick()
        render.vertex_list.vertices = render.world.vertices
        render.vertex_list.colors = render.world.colors

    @window.event
    def on_draw():
        render.window.clear()
        render.batch.draw()

    @window.event
    def on_key_press(symbol, modifiers):
        pass

    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            pass
        if buttons & mouse.RIGHT:
            pass

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            pass
        if button == mouse.RIGHT:
            pass

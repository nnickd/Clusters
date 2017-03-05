import colorsys
import numpy as np


class color:

    def rgb(r, g, b):
        return np.array([r, g, b])

    def hsv(h, s, v):
        return np.array(colorsys.hsv_to_rgb(h / 360, s, v)) * 255

    def hue_to_rgb(h):
        return color.hsv(h, 1, 1)

    def rgb_to_hue(rgb):
        c = rgb / 255
        return colorsys.rgb_to_hsv(*c)[0] * 360

    def random_rgb(r=(0, 255), g=(0, 255), b=(0, 255)):
        red = np.random.randint(r[1] - r[0] + 1) + r[0]
        green = np.random.randint(g[1] - g[0] + 1) + g[0]
        blue = np.random.randint(b[1] - b[0] + 1) + b[0]
        return color.rgb(red, green, blue)

    def random_hue(low, high):
        hue = np.random.randint(high - low) + low
        return color.hue_to_rgb(hue)

    def rotate(rgb, angle):
        hue = color.rgb_to_hue(rgb) + angle
        return color.hue_to_rgb(hue)

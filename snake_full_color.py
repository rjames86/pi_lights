import time
import board
import neopixel
from random import shuffle

pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 50

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False
)

def fade(pixels, duration, start_color, end_color):
    # G R B
    red_diff = end_color[1] - start_color[1]
    green_diff = end_color[0] - start_color[0]
    blue_diff = end_color[2] - start_color[2]

    delay = 0.005
    steps = int(duration // delay)

    for i in range(steps):
        red_value = start_color[1] + (red_diff * i // steps)
        green_value = start_color[0] + (green_diff * i // steps)
        blue_value = start_color[2] + (blue_diff * i // steps)

        pixels.fill((green_value, red_value, blue_value))
        pixels.show()
        time.sleep(delay)


RED = (0, 255, 0)
BLUE = (0, 0, 255)
GREEN = (255, 0, 0)
YELLOW = (255, 255, 0)
AQUA = (255, 0, 255)
PURPLE = (0, 128, 128)
GOLD = (215, 255, 0)
WHITE = (255, 255, 255)
MAGENTA = (0, 255,255)
PINK = (192, 255,203)
BLACK = (0,0,0)
DODGER_BLUE = (144, 30,255)
ORANGE = (165, 255,0)

# intentionally 10 colors so it's 5 lights per "rope"
ALL_COLORS = [
    DODGER_BLUE,
    WHITE,
    RED,
    BLUE,
    GREEN,
    YELLOW,
    AQUA,
    ORANGE,
    PURPLE,
    GOLD,
    WHITE,
    MAGENTA,
    PINK,
]

def fade_pixel(pixels, duration, index, new_color):
    start_color = pixels[index]
    # G R B
    red_diff = new_color[1] - start_color[1]
    green_diff = new_color[0] - start_color[0]
    blue_diff = new_color[2] - start_color[2]

    delay = 0.005
    steps = int(duration // delay)

    for i in range(steps):
        red_value = start_color[1] + (red_diff * i // steps)
        green_value = start_color[0] + (green_diff * i // steps)
        blue_value = start_color[2] + (blue_diff * i // steps)

        pixels[index] = (green_value, red_value, blue_value)
        pixels.show()
        time.sleep(delay)

def rainbow_circle():
    shuffle(ALL_COLORS)

    pixels.fill(0)
    pixels.show()
    for i in range(10000):
        for j in range(num_pixels):
            pixel_index = (i+j) % num_pixels
            color_value = j // (num_pixels // 10) % len(ALL_COLORS)
            pixels[pixel_index] = ALL_COLORS[color_value]
            # fade_pixel(pixels, 0.2, pixel_index, ALL_COLORS[color_value])
        pixels.show()
        time.sleep(0.25)

rainbow_circle()


# shuffle(ALL_COLORS)
# current_color = BLACK
# while True:
#     for color in ALL_COLORS:
#         fade(10, current_color, color)
#         current_color = color
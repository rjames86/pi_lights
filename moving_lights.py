import time
import board
import neopixel

pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 50

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False
)


def snake(pixels):
    line_length = 5
    wait = 0.001
    for i in range(len(pixels)+1):
        pixels.fill((0,0,0))
        pixels[i: i+line_length] = [(255, 0, 0) for i in range(i, i+line_length)]
        pixels.show()
        time.sleep(wait)

    for i in range(len(pixels)+1, -3, -1):
        pixels.fill((0,0,0))
        pixels[i: i+line_length] = [(255, 0, 0) for i in range(i, i+line_length)]
        pixels.show()
        time.sleep(wait)

# def snake_white(pixels):
WHITE = (255, 255, 255)
GREEN = (255, 0, 0)
RED = (0, 255, 0)
BLUE = (0, 0, 255)

class MovingLight:
    def __init__(self, color=BLUE):
        self.wait = 0.1
        self.line_length = 5
        self.iterations = 1
        self.color = color

    def move_lights(self):
        for _ in range(self.iterations):
            for i in range(25):
                pixels.fill(self.color)
                pixel_start = i % self.line_length
                for j in range(pixel_start, len(pixels), self.line_length):
                    pixels[j] = WHITE
                pixels.show()
                time.sleep(self.wait)
        time.sleep(0.5)
        for _ in range(self.iterations):
            for i in range(25)[::-1]:
                pixels.fill(self.color)
                pixel_start = i % self.line_length
                for j in range(pixel_start, len(pixels), self.line_length):
                    pixels[j] = WHITE
                pixels.show()
                time.sleep(self.wait)
        time.sleep(0.5)

m = MovingLight()

while True:
    m.move_lights()

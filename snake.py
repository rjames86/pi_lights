import time
import board
import neopixel

pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 50

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False
)


def snake(pixels, color):
    line_length = 5
    wait = 0.01
    for i in range(len(pixels)+1):
        pixels.fill((0,0,0))
        pixels[i: i+line_length] = [color for i in range(i, i+line_length)]
        pixels.show()
        time.sleep(wait)

    for i in range(len(pixels), -3, -1):
        pixels.fill((0,0,0))
        pixels[i: i+line_length] = [color for i in range(i, i+line_length)]
        pixels.show()
        time.sleep(wait)


for i in [(250,0,0), (0,250,0), (0,0,250)]:
    snake(pixels, i)

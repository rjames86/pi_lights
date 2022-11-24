import time
import board
import neopixel

pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 50

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False
)

RED = (0, 255, 0)
GREEN = (255, 0, 0)

def main():
    count = 0
    colors = (RED, GREEN)

    # This makes it loop forever until you stop the script
    while True:
        # Since there's only two colors, we want to alternate the count
        # between the numbers 0 and 1. 
        # Example: when count is 0, count + 1 is 1, and 1 % 2 is 1.
        # The next time around, count will be 1, so 1 + 1 = 2, 2 % 2 = 0
        count = (count + 1) % 2

        # If we get the (count % 2) color, it'll always be the opposite of count
        # That's how you can swap between colors
        pixels.fill(colors[count % 2])

        pixels.show()

        # Wait a half second
        time.sleep(0.5)

try:
    main()
# This part will shut off the pixels when you hit control-c
except KeyboardInterrupt:
    print("shutting off pixels...")
    pixels.fill((0, 0, 0))
    pixels.show()

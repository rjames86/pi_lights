import time
from rpi_ws281x import PixelStrip, Color

LED_COUNT = 50        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def jumper(strip, color, wait_ms=500):
    for i in range(0, strip.numPixels(), 2):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
        if i > 1:
            strip.setPixelColor(i, 0)
            strip.setPixelColor(i - 1, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            strip.setPixelColor(i-1, 0)


def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
    for i in range(strip.numPixels(), 0, -1):
        strip.setPixelColor(i, 0)
        strip.show()
        time.sleep(wait_ms / 1000.0)

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
strip.begin()
jumper(strip, Color(255,0,0))

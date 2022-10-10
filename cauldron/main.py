from machine import Pin
from neopixel import Neopixel
from neotimer import *
import random
import time
import micropython
import _thread

num_pixels = 27
base_fire_brightness = 25
base_cauldron_brightness = 100
fire_start = 0
fire_end = 12
cauldron_start = 14
cauldron_end = num_pixels
pixels = Neopixel(27, 0, 28, "RGB")
pixels.brightness(base_fire_brightness)
pixels.show

ORANGE = (255, 97, 3)
RED = (255, 0, 0)
WHITE = (255, 204, 229)
YELLOW = (255, 97, 3)
GREEN = (0, 255, 0)
GREEN2 = (100, 255, 0)
GREEN3 = (200, 255, 0)

# fire_leds = [WHITE, RED, YELLOW, RED, ORANGE, YELLOW, RED, ORANGE]
# cauldron_leds = [WHITE, GREEN, GREEN2, GREEN, GREEN3, GREEN, GREEN2, GREEN3]
fire_led_options = [WHITE, RED, YELLOW, ORANGE, YELLOW, ORANGE, RED]
cauldron_led_options = [GREEN, GREEN2, GREEN3]
fire_leds = list()
cauldron_leds = list()
fire_timer = Neotimer(50)
cauldron_timer = Neotimer(250)

def show_fire():
    global fire_timer
    if not fire_timer.waiting():
        fire_timer = Neotimer(random.randint(1, 80))
        fire_timer.start()
        
    if fire_timer.finished():
        for x in range(fire_start, fire_end):
            if fire_leds[x] == WHITE:
                pixels.set_pixel(x, fire_leds[x], (random.randint(0, 100)))
            else:                
                pixels.set_pixel(x, fire_leds[x], (random.randint(0, 120) + base_fire_brightness))
        y = random.randint(0, 80)
        if y == 0:
            fire_reset()
        pixels.show()
        
def fire_setup():
    for x in range(fire_start, fire_end):
        fire_leds.append(fire_led_options[random.randint(0, len(fire_led_options) - 1)])
    
def fire_reset():
    print('fire reset')
    fire_leds.clear()
    fire_setup()

def cauldron_reset():
    print('cauldron reset')
    cauldron_leds.clear()
    cauldron_setup()
    
def cauldron_setup():
    
    for x in range(cauldron_start, cauldron_end):
        cauldron_leds.append(cauldron_led_options[random.randint(0, len(cauldron_led_options) - 1)])

def show_cauldron():
    while True:
        if not cauldron_timer.waiting():
            cauldron_timer.start()
        
        if cauldron_timer.finished():
            for x in range(cauldron_start - fire_end - 1, cauldron_end - fire_end - 1):
                pixels.set_pixel(x + fire_end + 1, cauldron_leds[x], (random.randint(0, 120) + base_cauldron_brightness))
            
            y = random.randint(0, 100)
            if y == 0:
                cauldron_reset()  
            pixels.show()

fire_setup()
cauldron_setup()
_thread.start_new_thread(show_cauldron, ())
while(True):
    show_fire()
    #show_cauldron()



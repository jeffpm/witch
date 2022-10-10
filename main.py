import random
from machine import Pin
from neopixel import Neopixel
from neotimer import *
import random
import time
import micropython

num_pixels = 22
brightness = 100
pixels = Neopixel(num_pixels, 0, 28, "RGB")
pixels.brightness(brightness)

class Mouth:
    def __init__(self):
        self.pixels=[0, 1, 2]
        self.brightness = 50
        self.color = (61, 80, 10)
        
    def clear(self):
        pixels.set_pixel_line(self.pixels[0], self.pixels[-1], (0, 0, 0), 0)
        pixels.show()

    def show_solid(self, brightness = 25):
        pixels.set_pixel_line(self.pixels[0], self.pixels[-1], self.color, brightness)
        pixels.show()

    def sleep(self):
        for b in range(self.brightness):
            pixels.set_pixel_line(self.pixels[0], self.pixels[-1], self.color, b)
            pixels.show()
            time.sleep(0.05)
        for b in range(self.brightness, 0, -1):
            pixels.set_pixel_line(self.pixels[0], self.pixels[-1], self.color, b)
            pixels.show()
            time.sleep(0.05)
        pixels.clear()
        pixels.show()
        time.sleep(0.75)
        
class Eyes:
    def __init__(self):
        self.pixels=[3, 4]
        self.brightness = 50
        self.colors = [(255, 0, 0), (153, 0, 0), (204, 18, 0), (255, 255, 255)]
        self.color = (0, 0, 0)
        
    def clear(self):
        pixels.set_pixel_line(self.pixels[0], self.pixels[-1], (0, 0, 0), 0)
        pixels.show()
        
    def show_solid(self):
        self.choose_color()
        pixels.set_pixel_line(self.pixels[0], self.pixels[-1], self.color, self.brightness)
        pixels.show()
        
    def wink(self):
        #winks either eye, or closes both
        eye = random.randint(0, 2)
        if eye == 2:
            pixels.set_pixel_line(self.pixels[0], self.pixels[-1], (0, 0, 0), self.brightness)
        else:
            pixels.set_pixel(self.pixels[eye], (0, 0, 0), self.brightness)
        pixels.show()
        time.sleep(0.5)
        
    def choose_color(self):
        self.color = self.colors[random.randint(0, len(self.colors) - 1)]
        
class Hat:
    def __init__(self):
        self.pixels=list(range(5, 22))
        self.brightness = 50
        self.color = (200, 0, 100)
        self.timer = Neotimer(1000)
    
    def clear(self):
        pixels.set_pixel_line(self.pixels[0], self.pixels[-1], (0, 0, 0), self.brightness)
        pixels.show()
    
    def show_solid(self):
        pixels.set_pixel_line(self.pixels[0], self.pixels[-1], self.color, self.brightness)
        pixels.show()
        
    def show_cycle(self):
        for x in self.pixels:
            self.clear()
            pixels.set_pixel(x, self.color, self.brightness)
            pixels.show()
            time.sleep(0.05)
    
    def show_blink(self, num_times = 5):
        for x in range(num_times):
            self.clear()
            time.sleep(0.75)
            self.show_solid()
            time.sleep(0.75)

class Coordinator:
    def __init__(self):
        self.mouth = Mouth()
        self.eyes = Eyes()
        self.hat = Hat()
        
    # everything on, with the occasional wink and hat blink
    def show_solid(self, num_time = 30):
        for x in range(3):
            self.mouth.show_solid(40)
            self.eyes.show_solid()
            
            self.hat.show_solid()
            y = random.randint(0, 3)
            if y == 0:
                print('blink')
                self.hat.show_blink()
            time.sleep(num_time/3)
            print('wink')
            self.eyes.wink()
            #self.hat.show_cycle()
        
    #  fades mouth in a sleeping manner   
    def show_sleep(self, repeat = 2):
        pixels.clear()
        for x in range(repeat):
            self.mouth.sleep()
            self.eyes.clear()
            self.hat.clear()
    
    # blinks eyes a few times and then holds
    def show_wakeup(self, num_time = 10):
        pixels.clear()
        self.eyes.show_solid()
        time.sleep(3)
        pixels.clear()
        pixels.show()
        time.sleep(0.2)
        self.eyes.show_solid()
        time.sleep(2)
        pixels.clear()
        pixels.show()
        time.sleep(0.2)
        self.eyes.show_solid()
        time.sleep(1)
        pixels.clear()
        pixels.show()
        time.sleep(0.2)
        self.eyes.show_solid()
        time.sleep(num_time)

coord = Coordinator()

while(True):
    x = random.randint(1, 5)
    print(f'sleep {x}')
    coord.show_sleep(x)
    x = random.randint(10, 45)
    print(f'wakeup {x}')
    coord.show_wakeup(x)
    x = random.randint(30, 120)
    print(f'solid {x}')
    coord.show_solid(x)



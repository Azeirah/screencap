import PIL.ImageGrab
import time
import os
import win32gui
import threading
from hotkeyListener import GlobalHotKeys
import math

f_name = input("What's the name of your capture? ")
if not os.path.exists(f_name):
    os.mkdir(f_name)
width = int(input("What's the width of your capture? type 0 for fullscreen "))
height = int(input("What's the height of your capture? "))
print("Press F4 to start capturing", "Press F5 to stop capturing", "Press F1 to take a single screenshot", sep="\n")
captures = []
capturing = True
lastcoords = None

def distance(coord, coord2):
    return math.sqrt(math.pow(coord[0] - coord2[0], 2) + math.pow(coord[1] - coord2[1], 2))

def getMouseCoords():
    point = win32gui.GetCursorPos()
    return point

def save(capture):
    print("saving", capture[1])
    capture[0].save(capture[1])
    print("saved", capture[1])

def saveAll():
    global captures
    print("Saving all captures")
    for capture in captures:
        save(capture)
    captures = []
    print("done saving")

@GlobalHotKeys.register(GlobalHotKeys.VK_F1)
def capture():
    global lastcoords
    if width and height:
        coords = getMouseCoords()
        if lastcoords:
            if distance(coords, lastcoords) < 7:
                coords = lastcoords
        box = (coords[0] - int(0.5 * width), coords[1] - int(0.5 * height), coords[0] + int(0.5 * width), coords[1] + int(0.5 * height))
        cap = PIL.ImageGrab.grab(box)
        lastcoords = coords
    else:
        cap = PIL.ImageGrab.grab()
    filename = os.path.join(f_name, "{0:.2f}".format(time.time()) + ".png")
    print(filename)
    if len(captures) > 5:
        saveAll()
    captures.append((cap, filename))

@GlobalHotKeys.register(GlobalHotKeys.VK_F4)
def start():
    def startCapture():
        print("Starting capturing")
        while capturing:
            capture()
            time.sleep(0.005)
        print("Stopped capturing")
        stop()
        saveAll()
    threading.Thread(target=startCapture).start()

@GlobalHotKeys.register(GlobalHotKeys.VK_F2)
def stop():
    GlobalHotKeys.running = False

@GlobalHotKeys.register(GlobalHotKeys.VK_F5)
def stopCapture():
    global capturing
    print("Stopping capturing")
    capturing = False

GlobalHotKeys.listen()
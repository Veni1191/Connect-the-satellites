import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = "Connect the satellites"

current_satellite = 0
start_time = 0
total_time = 0
number_of_satellites = 10

satellites = []
lines = []

def create_satellites():
    global start_time, satellites
    for i in range(number_of_satellites):
        satellite = Actor("satellite")
        satellite.pos = randint(40,760),randint(40,560)
        satellites.append(satellite)
    start_time = time()

def draw():
    global total_time
    screen.blit("bg",(0,0))
    num = 1
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(num),(satellite.pos[0],satellite.pos[1]+20))
        num = num + 1 
    
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    
    if current_satellite < number_of_satellites:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time, 1)),(10,10),fontsize = 30)
    else:
        screen.draw.text(str(round(total_time, 1)),(10,10),fontsize = 30)
        







def update():
    pass

def on_mouse_down(pos):
    global current_satellite,lines
    if current_satellite < number_of_satellites:
        if satellites[current_satellite].collidepoint(pos):
            if current_satellite > 0:
                lines.append((satellites[current_satellite-1].pos,satellites[current_satellite].pos))
            current_satellite += 1 
        else: 
            lines = []
            current_satellite = 0




create_satellites()
pgzrun.go()
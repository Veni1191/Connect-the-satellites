import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = "Connect the wifi network"

current_wifi = 0
start_time = 0
total_time = 0
number_of_wifi = 8

wifis = []
connections = []

def create_wifi():
    global start_time, wifi
    for i in range(number_of_wifi):
        wifi = Actor("wifi")
        wifi.pos = randint(40,650),randint(40,560)
        wifis.append(wifi)
    start_time = time()

def draw():
    global total_time
    screen.blit("bg",(0,0))
    num = 1
    for wifi in wifis:
        wifi.draw()
        screen.draw.text(str(num),(wifi.pos[0],wifi.pos[1]+30))
        num = num + 1 
    
    for connection in connections:
        screen.draw.line(connection[0],connection[1],"white")
    
    if current_wifi < number_of_wifi:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time, 1)),(10,10),fontsize = 30)
    else:
        screen.draw.text(str(round(total_time, 1)),(10,10),fontsize = 30)
        

def update():
    pass

def on_mouse_down(pos):
    global current_wifi,connections
    if current_wifi < number_of_wifi:
        if wifis[current_wifi].collidepoint(pos):
            if current_wifi > 0:
                connections.append((wifis[current_wifi-1].pos,wifis[current_wifi].pos))
            current_wifi += 1 
        else: 
            connections = []
            current_wifi = 0




create_wifi()

pgzrun.go()
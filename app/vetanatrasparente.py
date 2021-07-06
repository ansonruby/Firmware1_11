


import os, sys, time, commands
import pygame
from pygame.locals import *


#--- Para Ventana grafica
DEBUG_Teclado = 0 # 0: ventana minimizada # 1: FULLSCREEN
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 480
win_pos_x=350
win_pos_y=100


pygame.init()

#-----      Configuracion de ventana   --------
if DEBUG_Teclado == 0:
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (win_pos_x, win_pos_y)
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
else:
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)







"""
import random
import sys
import threading

import pygame


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
FPS = 60


def circulos(draw_circles_event):
    circulos = [{'x': random.randint(0, WINDOW_WIDTH),
                 'y': random.randint(0, WINDOW_HEIGHT),
                 'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 'vel': random.randint(1, 5)}
                 for _ in range(1000)
                ]

    black = (0, 0, 0)

    clock = pygame.time.Clock()

    while draw_circles_event.is_set():
        surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT ))
        for circulo in circulos:
            posx = circulo["x"]
            color = circulo["color"]
            posy = circulo["y"]
            posy += circulo["vel"]
            if posy > WINDOW_HEIGHT:
                posy = 0
            pygame.draw.circle(surface, color, (posx, posy), 10, 0)
            circulo["y"] = posy

        event = pygame.event.Event(pygame.USEREVENT + 1,
                                   {"bitmap": surface}
                                   )
        pygame.event.post(event)
        clock.tick_busy_loop(FPS)


def main():
    pygame.init()
    pygame.display.set_caption("Circles Down")
    window  = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),
                                    pygame.HWSURFACE | pygame.DOUBLEBUF
                                    )

    draw_circles_event = threading.Event()
    draw_circles_event.set()
    hilo = threading.Thread(target=circulos, args=(draw_circles_event, ), daemon=True)
    hilo.start()


    circles_surface = None

    clock = pygame.time.Clock()

    # mainloop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.USEREVENT + 1:
                circles_surface = event.bitmap

        if circles_surface is not None:
            window.blit(circles_surface, (0, 0))

        pygame.display.flip()
        clock.tick_busy_loop(FPS)

    draw_circles_event.clear()
    pygame.quit()


if __name__ == "__main__":
    main()
"""

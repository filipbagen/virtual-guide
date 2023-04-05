import pygame
import sys
from pygame.locals import *


def test(FaceXPos, FaceYPos):

    #

    return  # Eyes position


def main(x, y):
    pygame.init()
    mainSurface = pygame.display.set_mode((500, 500), 0, 32)

    pygame.display.set_caption("Bouncing Ball")
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    block = pygame.Surface((50, 50))
    rect = block.get_rect()
    # circle =
    block.fill(RED)
    # speedx = 3  # Fixed horizontal velocity of 3 pixels per frame
    # speedy = 2  # Fixed vertical velocity of 2 pixels per frame

    # object current co-ordinates
    x = 200
    y = 200

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        mainSurface.fill(WHITE)
        # rect.top += speedy
        # rect.left += speedx

        # if rect.top < 0 or rect.bottom > 500:
        #     speedy = -speedy

        # if rect.left < 0 or rect.right > 500:
        #     speedx = -speedx

        # mainSurface.blit(block, rect)
        # pygame.draw.rect(mainSurface, (255, 0, 0), (x, y, 50, 50))
        pygame.draw.circle(mainSurface, (0, 0, 0), (x, y), 50)
        pygame.display.update()


main(100, 100)

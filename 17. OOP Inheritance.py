import random

import pygame
from Blob import Blob

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


class BlueBlob(Blob):
    def __init__(self, x_bound, y_bound):
        super().__init__(color=BLUE, x_bound=x_bound, y_bound=y_bound)

class RedBlob(Blob):
    def __init__(self, x_bound, y_bound):
        super().__init__(color=RED, x_bound=x_bound, y_bound=y_bound)

    def moveFast(self):
        self.x += random.randrange(-7,7)
        self.y += random.randrange(-7,7)
def draw_environemnt(blob_list):
    game_display.fill(WHITE)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.checkBounds()
    pygame.display.update()


def main():
    blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))

    print(blue_blobs)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environemnt([blue_blobs, red_blobs])
        clock.tick(60)


if __name__ == '__main__':
    main()

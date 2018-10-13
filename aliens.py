import pygame
import time
import random

objCount = 0


class aliens():
    '''pass image, screen, dimensions'''

    def __init__(self, img, screen, dim):
        global objCount
        tmp = objCount
        objCount = tmp + 1
        print(objCount)
        self.en = time.time() + 8
        self.f = 0
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (dim, dim))
        self.x = random.randrange(50, screen.get_width() - 100, 100)
        self.y = random.randrange(10, 210, 100)

    def __str__(self):
        print(objCount)
        return self.image + " " + self.x + " " + self.y

    def __del__(self):
        global objCount
        tmp = objCount
        objCount = tmp - 1
        print("deleted, objCount={0}".format(objCount))

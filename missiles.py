import pygame


class missile():
    def __init__(self, x, y, img, dim):
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (dim, dim))
        self.x = x
        self.y = y


class mis1(missile):
    def __init__(self, img, x, y, dim):
        self.type = 1
        self.speed = 2
        missile.__init__(self, x, y, img, dim)


class mis2(missile):
    def __init__(self, img, x, y, dim):
        self.type = 2
        self.speed = 4
        missile.__init__(self, x, y, img, dim)

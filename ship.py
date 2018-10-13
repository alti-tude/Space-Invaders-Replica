import pygame


class ship():
    def __init__(self, img, screen, dim, bot):
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (dim, dim))
        self.x = screen.get_width() / 2 - self.image.get_width() / 2
        self.y = screen.get_height() - self.image.get_height() - bot

    def __str__(self):
        return (str(self.image) + " " + str(self.x) + " " + str(self.y))

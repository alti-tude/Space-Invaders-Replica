import pygame
import sys
import time
import aliens
import ship
import missiles

pygame.init()
pygame.display.set_caption("ALIEN ATTACK")
stTime = time.time()
initTime = time.time()
count = 0

# font for score
myfont = pygame.font.SysFont("monospace", 30)
WHITE = (255, 255, 255)
score = myfont.render("SCORE={0}".format(count), 1, WHITE)

screen = pygame.display.set_mode((800, 800))
spaceShip = ship.ship("images/ship.png", screen, 100, 50)
screen.fill((0, 0, 0))

screen.blit(spaceShip.image, (spaceShip.x, spaceShip.y))
pygame.display.update()

alien = []
miss = []
alien.append(aliens.aliens("images/aliens.jpg", screen, 100))
while 1:
    pygame.time.Clock().tick(50)
    flag = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if spaceShip.x > 50:
                    spaceShip.x -= 100
            elif event.key == pygame.K_d:
                if spaceShip.x < screen.get_width() - 150:
                    spaceShip.x += 100
            elif event.key == pygame.K_w:
                miss.append(missiles.mis1("images/missile.png",
                                          spaceShip.x + 25, spaceShip.y, 50))
            elif event.key == pygame.K_s:
                miss.append(missiles.mis2("images/missile2.png",
                                          spaceShip.x + 25, spaceShip.y, 50))
            elif event.key == pygame.K_q:
                sys.exit()
            flag = 1

    screen.fill((0, 0, 0))

    # collision system for missiles
    for m in miss:
        flag = 0
        for a in alien:
            if m.y - a.y <= 50 and m.x == a.x + 25:
                print("deleted by colission")
                if m.type == 1:
                    alien.remove(a)
                    count += 1
                    score = myfont.render("SCORE={0}".format(count), 1, WHITE)
                    flag = 1
                elif a.f != 1:
                    a.image = pygame.image.load("images/aliens2.jpg")
                    a.image = pygame.transform.scale(a.image, (100, 100))
                    a.en = time.time() + 5
                    a.f = 1
                    flag = 1
                break
        if flag != 1:
            m.y -= m.speed
            if m.y <= 0:
                miss.remove(m)
            else:
                screen.blit(m.image, (m.x, m.y))
        else:
            miss.remove(m)

    # spawn alien
    if time.time() - stTime >= 10:
        alien.append(aliens.aliens("images/aliens.jpg", screen, 100))
        stTime = time.time()

    # move ship
    screen.blit(spaceShip.image, (spaceShip.x, spaceShip.y))

    # update score
    scX = screen.get_width() / 2 - score.get_width() / 2
    scY = screen.get_height() / 2 - score.get_height() / 2
    screen.blit(score, (scX, scY))

    # update aliens
    for i in alien:
        if time.time() < i.en:
            screen.blit(i.image, (i.x, i.y))
        else:
            alien.remove(i)
    pygame.display.update()

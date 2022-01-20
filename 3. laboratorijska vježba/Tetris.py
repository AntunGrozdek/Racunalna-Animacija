import time

import pygame
import random
import sys

WIDTH, HEIGHT = 600, 960
width, height = 400, 800
block_size = 40
next_block_size = 20
clock = pygame.time.Clock()
shape_x = 3
shape_y = 0
rotation = 0
START = 0
SCORE = 0

save = []

I = [[1, 5, 9, 13], [4, 5, 6, 7]]
O = [[1, 2, 5, 6]]
T = [[1, 4, 5, 6], [1, 5, 6, 9], [4, 5, 6, 9], [1, 4, 5, 9]]
J = [[1, 5, 8, 9], [1, 2, 3, 7], [1, 2, 5, 9], [1, 5, 6, 7]]
L = [[1, 2, 6, 10], [2, 4, 5, 6], [1, 5, 9, 10], [1, 2, 3, 5]]
S = [[1, 2, 4, 5], [1, 5, 6, 10]]
Z = [[1, 2, 6, 7], [1, 4, 5, 8]]

shapes = [I, O, T, J, L, S, Z]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("TETRIS")

flag = 0
flag2 = 1

# polje = []


def polje_igre():
    polje = []
    for i in range(20):
        linija = []
        for j in range(10):
            linija.append(0)
        polje.append(linija)
    return polje


def provjera(now):
    greska = False
    for i in range(4):
        for j in range(4):
            if i * 4 + j in now:
                if i + shape_y > 19 or j + shape_x > 9 or j + shape_x < 0 or polje[i + shape_y][j + shape_x] > 0:
                    greska = True
    return greska


def pocisti_red(SCORE):
    linije = 0
    for i in range(1, 20):
        nule = 0
        for j in range(10):
            if polje[i][j] == 0:
                nule += 1
        if nule == 0:
            linije += 1
            for k in range(i, 1, -1):
                for j in range(10):
                    polje[k][j] = polje[k - 1][j]
    SCORE += linije
    return SCORE


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_r:
                shape_x = 3
                shape_y = 0
                rotation = 0
                START = 0
                SCORE = 0
                flag = 0
                flag2 = 1
            if event.key == pygame.K_RIGHT:
                old_x = shape_x
                shape_x += 1
                if provjera(now):
                    shape_x = old_x

            if event.key == pygame.K_LEFT:
                old_x = shape_x
                shape_x -= 1
                if provjera(now):
                    shape_x = old_x

            if event.key == pygame.K_DOWN:
                shape_y += 1

                if provjera(now):
                    shape_y -= 1
                    for i in range(4):
                        for j in range(4):
                            if i * 4 + j in now:
                                polje[i + shape_y][j + shape_x] += 1
                    SCORE = pocisti_red(SCORE)
                    shape_x, shape_y, rotation = 3, 0, 0
                    type = type_next
                    now = next
                    type_next = random.randint(0, len(shapes) - 1)
                    next = shapes[type_next][rotation]
                    if provjera(now):
                        START = 1

            if event.key == pygame.K_UP:
                old_rotation = rotation
                rotation = (rotation + 1) % len(shapes[type])
                if provjera(now):
                    rotation = old_rotation

            if event.key == pygame.K_c:
                flag2 = 0

    if START == 0:
        screen.fill((0, 0, 0))

        if flag == 0:
            polje = polje_igre()

        for i in range(20):
            for j in range(10):
                pygame.draw.rect(screen, (128, 128, 128), [50 + block_size * j, 50 + block_size * i, block_size, block_size], 1)
                if polje[i][j] > 0:
                    pygame.draw.rect(screen, (128, 128, 128), [50 + block_size * j +1, 50 + block_size * i + 1, block_size - 2, block_size - 1])

        pygame.draw.rect(screen, (128, 128, 128), [450 + block_size, 50, block_size * 2, block_size * 2], 1)
        pygame.draw.rect(screen, (128, 128, 128), [450 + block_size, 50 + block_size * 4, block_size * 2, block_size * 2], 1)

        if flag == 0:
            polje = polje_igre()
            type = random.randint(0, len(shapes) - 1)
            type_next = random.randint(0, len(shapes) - 1)
            now = shapes[type][rotation]
            next = shapes[type_next][rotation]
            flag = 1
        elif flag == 1:
            now = shapes[type][rotation]

        if flag2 == 0:
            shape_x = 3
            shape_y = 0
            rotation = 0
            if not save:
                type_save = type
                type = type_next
                save = now
                now = next
                type_next = random.randint(0, len(shapes) - 1)
                next = shapes[type_next][rotation]
            else:
                pom_type = type_save
                type_save = type
                type = pom_type
                pom = save
                save = now
                now = pom
            flag2 = 1

        COLOR = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in now:
                    pygame.draw.rect(screen, COLOR, [50 + block_size * (j + shape_x) + 1, 50 + block_size * (i + shape_y) + 1, block_size - 2, block_size - 2])
                if p in next:
                    pygame.draw.rect(screen, (255, 255, 255), [450 + block_size + next_block_size * j + 1, 50 + block_size * 4 + next_block_size * i + 1, next_block_size - 2, next_block_size - 2])
                if p in save:
                    pygame.draw.rect(screen, (255, 255, 255), [450 + block_size + next_block_size * j + 1, 50 + next_block_size * i + 1, next_block_size - 2, next_block_size - 2])

        shape_y += 1

        if provjera(now):
            shape_y -= 1
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in now:
                        polje[i + shape_y][j + shape_x] += 1
            SCORE = pocisti_red(SCORE)
            shape_x, shape_y, rotation = 3, 0, 0
            type = type_next
            now = next
            type_next = random.randint(0, len(shapes) - 1)
            next = shapes[type_next][rotation]
            if provjera(now):
                START = 1

        font = pygame.font.SysFont('Calibri', 25, True, False)
        score = font.render("Score: " + str(SCORE), True, (255, 255, 255))
        change = font.render("Change: ", True, (255, 255, 255))
        next_shape = font.render("Next: ", True, (255, 255, 255))
        screen.blit(score, [50, 900])
        screen.blit(change, [488, 25])
        screen.blit(next_shape, [488, 185])

        font_2 = pygame.font.SysFont('Calibri', 50, True, False)
        lost = font_2.render("YOU LOST!", True, (255, 0, 0))
        new_game = font_2.render("Press R for new game!", True, (255, 0, 0))
        if START == 1:
            screen.blit(lost, [200, 400])
            screen.blit(new_game, [80, 450])

    pygame.display.flip()
    clock.tick(4)

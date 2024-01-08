import pygame


def player_walking_x(x):
    player_speed = 30
    player_x = x
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and player_x < 1200:
        player_x += player_speed

    elif keys[pygame.K_a] and player_x > 200:
        player_x -= player_speed
    return player_x


def player_jumping_y(player_y, is_jump, jump_count):
    keys = pygame.key.get_pressed()
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count >= 0:
                player_y -= (jump_count ** 2) // 2
                jump_count -= 1
            else:
                player_y += (jump_count ** 2) // 2
                jump_count -= 1

        else:
            jump_count = 10
            is_jump = False
    return player_y,is_jump,jump_count

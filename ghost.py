def ghost_func(ghost,speed,image,rect,screen):
    ghost_list = ghost
    bistree = speed
    ghost_image = image
    player_rect = rect
    screen = screen
    if ghost_list:
        for el in ghost_list:
            screen.blit(ghost_image, el),
            el.x -= bistree
            if player_rect.colliderect(el):
                return 2
def game_1_screen(screen, knight_image, label_skin_1, label_back, knight_image2, label_skin_2, knight_image3,
                  label_skin_3, label_skin_4, knight_image4, knight_image5, label_skin_5):
    screen.fill((128, 140, 136))
    screen.blit(knight_image, (200, 250))
    screen.blit(label_skin_1, (200, 350))
    screen.blit(label_back, (100, 500))
    screen.blit(knight_image2, (400, 250))
    screen.blit(label_skin_2, (400, 350))
    screen.blit(knight_image3, (600, 250))
    screen.blit(label_skin_3, (600, 350))
    screen.blit(knight_image4, (800, 250))
    screen.blit(label_skin_4, (800, 350))
    screen.blit(knight_image5, (1000, 250))
    screen.blit(label_skin_5, (1000, 350))

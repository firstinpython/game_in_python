import pygame


def gameplay(game, km, result, screen, background_image, background_x, run_sprite, sprites_counter, player_x, player_y,
             label_result, zabor, bistree, ghost_func, ghost_list, ghost_image, money, money_list, money_image, base,
             player_walking_x, player_jumping_y, is_jump, jump_count, knight, knight_list, defaultknight):
    if game == 0:
        km += 1
        result += 1
        screen.blit(background_image, (background_x, 0))
        screen.blit(background_image, (background_x + 1275, 0))
        screen.blit(run_sprite[sprites_counter], (player_x, player_y))
        player_rect = run_sprite[0].get_rect(topleft=(player_x, player_y))
        screen.blit(label_result, (100, 100))
        if result >= zabor:
            bistree += 10
            zabor += 1000
        if ghost_func(ghost_list, bistree, ghost_image, player_rect, screen) == 2:
            game = 2
        if money(money_list, money_image, player_rect, screen, base) == 100:
            result += 100

        player_x = player_walking_x(player_x)
        keys = pygame.key.get_pressed()
        player_y, is_jump, jump_count = player_jumping_y(player_y, is_jump, jump_count)
        if knight(knight_list, screen, defaultknight, ghost_list) == 100:
            result += 100
        if sprites_counter < len(run_sprite) - 1:
            sprites_counter += 1
        else:
            sprites_counter = 0
        if background_x != -1400:
            background_x -= 2
        else:
            background_x = 0
    return game, km, result, screen, background_image, background_x, run_sprite, sprites_counter, player_x, player_y, label_result, zabor, bistree, ghost_list, ghost_image, money_list, money_image, is_jump, jump_count, knight_list, defaultknight


def lose_label_func(game, knight_list, money_list, screen, lose_label, menu_label, base, result, label, lose_label_rect,
                    ghost_list, mouse, menu_label_rect, ghost_speed, player_x, score_flag):
    if game == 2:
        ghost_speed = 10
        knight_list.clear()
        money_list.clear()
        screen.fill((128, 140, 136))
        screen.blit(lose_label, (500, 250))
        screen.blit(menu_label, (500, 350))

        if base.score(result) == 1:
            score_flag = True
            base.update_score(result)

        if score_flag == True:
            label_score = label.render(f'Your score {result}', False, (193, 196, 199))
            screen.blit(label_score, (350, 100))

        if lose_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            game = 0
            player_x = 300
            result = 0
            score_flag = False
            ghost_list.clear()
        if menu_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            result = 0
            game = 3
            score_flag = False
    return game, knight_list, money_list, screen, result, ghost_list, ghost_speed, player_x, score_flag


def arsenal(label_skin_1, base, defaultknight, knight_image, is_knight, label_skin_2, knight_image2,
            label_skin_3, knight_image3, label_skin_4, knight_image4, label_skin_5, knight_image5, screen, is_buy,
            no_money, name_knight, game):
    label_skin_1_rect = label_skin_1.get_rect(topleft=(200, 350))
    label_skin_2_rect = label_skin_2.get_rect(topleft=(450, 350))
    label_skin_3_rect = label_skin_3.get_rect(topleft=(600, 350))
    label_skin_4_rect = label_skin_4.get_rect(topleft=(750, 350))
    label_skin_5_rect = label_skin_5.get_rect(topleft=(900, 350))
    mouse = pygame.mouse.get_pos()
    if game == 1:
        if label_skin_1_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            skin = 'skin_1'
            name_knight = 'алмазный меч'
            a = base.buy(skin)
            if int(a) == 1:
                is_buy = True
            elif int(a) == 2:
                no_money = True
            elif int(a) == 3:
                what_skin = base.proverka(knight_image, knight_image2, knight_image3, knight_image4, knight_image5)[0]
                if what_skin != 'skin_1':
                    base.skins('skin_1', what_skin)
                    defaultknight = knight_image
                    is_knight = True
        elif label_skin_2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            skin = 'skin_2'
            name_knight = 'древесный нож'
            a = base.buy(skin)
            if int(a) == 1:
                is_buy = True
            elif int(a) == 2:
                no_money = True
            elif int(a) == 3:
                what_skin = base.proverka(knight_image, knight_image2, knight_image3, knight_image4, knight_image5)[0]
                if what_skin != 'skin_2':
                    base.skins('skin_2', what_skin)
                    defaultknight = knight_image2
                    is_knight = True
        elif label_skin_3_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            skin = 'skin_3'
            name_knight = 'золотой меч'
            a = base.buy(skin)
            if int(a) == 1:
                is_buy = True
            elif int(a) == 2:
                no_money = True
            elif int(a) == 3:
                what_skin = base.proverka(knight_image, knight_image2, knight_image3, knight_image4, knight_image5)[0]
                if what_skin != 'skin_3':
                    base.skins('skin_3', what_skin)
                    defaultknight = knight_image3
                    is_knight = True

        elif label_skin_4_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            skin = 'skin_4'
            name_knight = 'демонический меч'
            a = base.buy(skin)
            if int(a) == 1:
                is_buy = True
            elif int(a) == 2:
                no_money = True
            elif int(a) == 3:
                what_skin = base.proverka(knight_image, knight_image2, knight_image3, knight_image4, knight_image5)[0]
                if what_skin != 'skin_4':
                    base.skins('skin_4', what_skin)
                    defaultknight = knight_image4
                    is_knight = True
        elif label_skin_5_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            skin = 'skin_5'
            name_knight = 'синий меч'
            a = base.buy(skin)
            if int(a) == 1:
                is_buy = True
            elif int(a) == 2:
                no_money = True
            elif int(a) == 3:
                what_skin = base.proverka(knight_image, knight_image2, knight_image3, knight_image4, knight_image5)[0]
                if what_skin != 'skin_5':
                    base.skins('skin_5', what_skin)
                    defaultknight = knight_image5
                    is_knight = True
    return base, defaultknight, is_knight, screen, is_buy, no_money, name_knight

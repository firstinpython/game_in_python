def menu(screen, label_play, label_arsenal, main_run,is_buy,no_money,is_knight,score_flag):
    screen.fill((128, 140, 136))
    screen.blit(label_play, (500, 250))
    screen.blit(label_arsenal, (500, 400))
    screen.blit(main_run, (100, 200))
    is_buy = False
    no_money= False
    is_knight = False
    score_flag = False
    return is_buy,no_money,is_knight,score_flag
def knight(knight_list,screen,defaultknight,ghost_list):
    money = 100
    if knight_list:
        for (i, el) in enumerate(knight_list):
            screen.blit(defaultknight, (el.x, el.y))
            el.x += 20
            if ghost_list:
                for (num, ghost1) in enumerate(ghost_list):
                    if el.colliderect(ghost1):
                        ghost_list.pop(num)
                        knight_list.pop(i)
                        return money

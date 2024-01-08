def money(money_list,money_image,player_rect,screen,base):
    money = 100
    if money_list:
        for i, el in enumerate(money_list):
            screen.blit(money_image, el)
            el.x -= 10
            if player_rect.colliderect(el):
                base.money(100)
                money_list.pop(i)
                return money
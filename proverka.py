def buy_arsenal(label,screen,name_knight):
    label_buy = label.render(f'Вы купили {name_knight}', False, (193, 196, 199))
    screen.blit(label_buy, (350, 150))
def money_arsenal(label,screen,name_knight):
    label_erros = label.render(f'недостаточно денег для {name_knight}', False, (193, 196, 199))
    screen.blit(label_erros, (350, 150))
def knight_arsenal(label,screen, name_knight):
    label_erros = label.render(f'Вы взяли {name_knight}', False, (193, 196, 199))
    screen.blit(label_erros, (350, 150))
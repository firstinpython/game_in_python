def buy_arsenal(label,screen):
    label_buy = label.render('Вы купили нож', False, (193, 196, 199))
    screen.blit(label_buy, (600, 400))
def money_arsenal(label,screen):
    label_erros = label.render('недостаточно денег', False, (193, 196, 199))
    screen.blit(label_erros, (600, 400))
def knight_arsenal(label,screen):
    label_erros = label.render('Вы взяли нож', False, (193, 196, 199))
    screen.blit(label_erros, (600, 400))
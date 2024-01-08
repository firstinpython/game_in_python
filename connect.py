import pygame
from run_sprites import sprites

def connect():
    label = pygame.font.Font('RubikDoodleShadow-Regular.ttf', 60)
    label_knight = pygame.font.Font('RubikDoodleShadow-Regular.ttf', 40)
    lose_label = label.render('Lose', False, (193, 196, 199))
    menu_label = label.render('Menu', False, (193, 196, 199))
    label_play = label.render('PLAY', False, (193, 196, 199))
    label_skin_1 = label_knight.render('Skin_1', False, (193, 196, 199))
    label_skin_2 = label_knight.render('Skin_2', False, (193, 196, 199))
    label_skin_3 = label_knight.render('Skin_3', False, (193, 196, 199))
    label_skin_4 = label_knight.render('Skin_4', False, (193, 196, 199))
    label_skin_5 = label_knight.render('Skin_5', False, (193, 196, 199))
    label_skin_6 = label_knight.render('Skin_6', False, (193, 196, 199))
    label_arsenal = label.render('Arsenal', False, (193, 196, 199))
    label_back = label.render('Back', False, (193, 196, 199))
    return label,label_knight,lose_label, menu_label, label_play, label_skin_1, label_skin_2, label_skin_3, label_skin_4, label_skin_5, label_skin_6, label_arsenal, label_back

def image():
    background_image = pygame.image.load('image/maxresdefault.jpg').convert()
    ghost_image = pygame.image.load('image/ghost_4.png').convert_alpha()
    knight_image = pygame.image.load('image/khights/knight_1.png').convert_alpha()
    knight_image2 = pygame.image.load('image/khights/knight_2.png').convert_alpha()
    knight_image3 = pygame.image.load('image/khights/knight_3.png').convert_alpha()
    knight_image4 = pygame.image.load('image/khights/knight_4.png').convert_alpha()
    knight_image5 = pygame.image.load('image/khights/knight_5.png').convert_alpha()
    knight_image6 = pygame.image.load('image/khights/knight_6.png').convert_alpha()
    money_image = pygame.image.load('image/money_1.png').convert_alpha()
    main_run = pygame.image.load('image/main_run.jpg').convert_alpha()
    return background_image,ghost_image,knight_image,knight_image2,knight_image3,knight_image4,knight_image5,knight_image6,money_image,main_run
def init_connect():
    run_sprite = sprites()
    sprites_counter = 0
    background_x = 0
    player_x = 300
    player_y = 470
    ghost_x = 1282
    is_jump = False
    jump_count = 10
    ghost_list = []
    money_list = []
    money_x = 1282
    result = 0
    knight_list = []
    run = True
    game = 3
    km = 0
    zabor = 1000
    ghost_speed = 10
    score_flag = False
    is_buy = False
    no_money = False
    is_knight = False
    return run_sprite,sprites_counter,background_x,player_x,player_y,ghost_x,is_jump,jump_count,ghost_list,money_list,money_x,result,knight_list,run,game,km,zabor,ghost_speed,score_flag,is_buy,no_money,is_knight

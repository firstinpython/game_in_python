import pygame
from sounds import back_sound
from walking_player import player_walking_x, player_jumping_y
from db import Base
from ghost import ghost_func
from money import money
from knight import knight
from menu import menu
from proverka import buy_arsenal, money_arsenal, knight_arsenal
from game_screen import game_1_screen
from game import gameplay, lose_label_func, arsenal
from connect import connect, image, init_connect


class Game:
    def __init__(self):
        self.base = Base('play_db')
        pygame.init()
        self.screen = pygame.display.set_mode((1275, 650))
        pygame.display.set_caption('Game')
        pygame.display.set_icon(pygame.image.load('image/run/run_1.png'))
        self.clock = pygame.time.Clock()
        self.background_image, self.ghost_image, self.knight_image, self.knight_image2, self.knight_image3, self.knight_image4, self.knight_image5, self.knight_image6, self.money_image, self.main_run = image()
        self.defaultknight = \
            self.base.proverka(self.knight_image, self.knight_image2, self.knight_image3, self.knight_image4,
                               self.knight_image5)[1]
        back_sound().play()
        self.run_sprite, self.sprites_counter, self.background_x, self.player_x, self.player_y, self.ghost_x, self.is_jump, self.jump_count, self.ghost_list, self.money_list, self.money_x, self.result, self.knight_list, self.run, self.game, self.km, self.zabor, self.ghost_speed, self.score_flag, self.is_buy, self.no_money, self.is_knight, self.name_knight = init_connect()
        self.ghost_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ghost_timer, 5000)
        self.money_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.money_timer, 3000)
        self.label, self.label_knight, self.lose_label, self.menu_label, self.label_play, self.label_skin_1, self.label_skin_2, self.label_skin_3, self.label_skin_4, self.label_skin_5, self.label_skin_6, self.label_arsenal, self.label_back = connect()

        self.gaming()

    def gaming(self):
        while self.run:
            label_play_rect = self.label_play.get_rect(topleft=(500, 200))
            self.lose_label_rect = self.lose_label.get_rect(topleft=(500, 250))
            self.menu_label_rect = self.menu_label.get_rect(topleft=(500, 350))
            label_arsenal_rect = self.label_arsenal.get_rect(topleft=(700, 200))
            label_back_rect = self.label_back.get_rect(topleft=(100, 500))
            self.label_result = self.label_knight.render(str(self.result), False, (193, 196, 199))
            if self.game == 3:
                menu_main = menu(self.screen, self.label_play, self.label_arsenal, self.main_run, self.is_buy,
                                 self.no_money, self.is_knight, self.score_flag)
                self.is_buy = menu_main[0]
                self.no_money = menu_main[1]
                self.is_knight = menu_main[2]
                self.score_flag = menu_main[3]
            self.mouse = pygame.mouse.get_pos()
            if label_play_rect.collidepoint(self.mouse) and pygame.mouse.get_pressed()[0] and self.game == 3:
                self.game = 0
                self.player_x = 300
                self.ghost_list.clear()
            if self.game == 0:
                (
                    self.game, self.km, self.result, self.screen, self.background_image, self.background_x,
                    self.run_sprite,
                    self.sprites_counter, self.player_x, self.player_y, self.label_result, self.zabor, self.ghost_speed,
                    self.ghost_list, self.ghost_image, self.money_list, self.money_image, self.is_jump, self.jump_count,
                    self.knight_list, self.defaultknight) = gameplay(
                    self.game, self.km, self.result, self.screen, self.background_image, self.background_x,
                    self.run_sprite,
                    self.sprites_counter, self.player_x, self.player_y, self.label_result, self.zabor, self.ghost_speed,
                    ghost_func,
                    self.ghost_list, self.ghost_image,
                    money, self.money_list,
                    self.money_image, self.base, player_walking_x,
                    player_jumping_y, self.is_jump, self.jump_count,
                    knight, self.knight_list,
                    self.defaultknight)
            self.game, self.knight_list, self.money_list, self.screen, self.result, self.ghost_list, self.ghost_speed, self.player_x, self.score_flag = lose_label_func(
                self.game, self.knight_list, self.money_list, self.screen, self.lose_label, self.menu_label, self.base,
                self.result, self.label, self.lose_label_rect, self.ghost_list, self.mouse, self.menu_label_rect,
                self.ghost_speed, self.player_x, self.score_flag)
            if label_arsenal_rect.collidepoint(self.mouse) and pygame.mouse.get_pressed()[0] and self.game == 3:
                self.game = 1

            if self.game == 1:
                game_1_screen(self.screen, self.knight_image, self.label_skin_1, self.label_back, self.knight_image2,
                              self.label_skin_2,
                              self.knight_image3, self.label_skin_3, self.label_skin_4, self.knight_image4,
                              self.knight_image5, self.label_skin_5)

                if label_back_rect.collidepoint(self.mouse) and pygame.mouse.get_pressed()[0]:
                    self.game = 3
                self.base, self.defaultknight, self.is_knight, self.screen, self.is_buy, self.no_money, self.name_knight = arsenal(
                    self.label_skin_1, self.base, self.defaultknight, self.knight_image, self.is_knight,
                    self.label_skin_2, self.knight_image2, self.label_skin_3, self.knight_image3, self.label_skin_4,
                    self.knight_image4, self.label_skin_5, self.knight_image5, self.screen, self.is_buy, self.no_money,
                    self.name_knight, self.game)

                if self.is_buy == True:
                    buy_arsenal(self.label_knight, self.screen, self.name_knight)
                    self.no_money = False
                    self.is_knight = False
                if self.no_money == True:
                    money_arsenal(self.label_knight, self.screen, self.name_knight)
                    self.is_buy = False
                    self.is_knight = False
                if self.is_knight == True:
                    knight_arsenal(self.label_knight, self.screen, self.name_knight)
                    self.is_buy = False
                    self.no_money = False

            pygame.display.update()
            for event in pygame.event.get():
                knight_rect = self.defaultknight.get_rect(topleft=(self.player_x, self.player_y))
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                if event.type == self.ghost_timer:
                    self.ghost_list.append(self.ghost_image.get_rect(topleft=(self.ghost_x, 500)))
                if event.type == self.money_timer:
                    self.money_list.append(self.money_image.get_rect(topleft=(self.money_x, 550)))
                if self.game == 0 and event.type == pygame.KEYUP and event.key == pygame.K_f:
                    self.knight_list.append(knight_rect)
            self.clock.tick(10)


if __name__ == "__main__":
    Game()

import pygame
from config import GameConfig
from game_map import GameMap
from player import Player
from enemy import EnemyManager
from boss import BossManager
from items import ItemManager
from ui import UIManager
from utilities import SaveManager


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT))
        pygame.display.set_caption(GameConfig.GAME_TITLE)
        self.clock = pygame.time.Clock()
        
        self.game_map = GameMap()
        self.player = Player()
        self.enemy_manager = EnemyManager()
        self.boss_manager = BossManager()
        self.item_manager = ItemManager()
        self.ui_manager = UIManager()
        
        self.save_manager = SaveManager()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.save_manager.save_game(self)
                return False
            # Add other input handling here, such as movement, menu navigation, etc.
        return True

    def update(self):
        self.player.update()
        self.enemy_manager.update()
        self.boss_manager.update()
        self.item_manager.update()
        self.ui_manager.update()

    def render(self):
        self.game_map.draw(self.screen)
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.boss_manager.draw(self.screen)
        self.item_manager.draw(self.screen)
        self.ui_manager.draw(self.screen)
        pygame.display.flip()

    def main_loop(self):
        running = True
        while running:
            self.clock.tick(GameConfig.FPS)
            running = self.handle_input()
            self.update()
            self.render()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    
    if game.save_manager.load_game(game):
        print("Game loaded successfully")
    else:
        print("New game started")
    
    game.main_loop()

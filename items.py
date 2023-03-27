import pygame
from config import GameConfig


class Item:
    def __init__(self, x, y, item_type):
        self.x = x
        self.y = y
        self.width = GameConfig.TILE_WIDTH
        self.height = GameConfig.TILE_HEIGHT
        self.item_type = item_type

    def use(self, user):
        # Implement item usage logic here, depending on the item type and user

    def draw(self, screen):
        pygame.draw.rect(screen, GameConfig.COLOR_ITEM, (self.x * GameConfig.TILE_WIDTH,
                                                          self.y * GameConfig.TILE_HEIGHT,
                                                          self.width, self.height))


class ItemManager:
    def __init__(self):
        self.items = []

    def spawn_items(self, game_map):
        # Implement item spawning logic here based on the game map

    def pick_up(self, item, user):
        # Implement item pick-up logic here
        self.items.remove(item)
        item.use(user)

    def update(self, game_map, player):
        for item in self.items:
            if item.x == player.x and item.y == player.y:
                self.pick_up(item, player)

    def draw(self, screen):
        for item in self.items:
            item.draw(screen)

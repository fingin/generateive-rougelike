import pygame
from config import GameConfig


class HealthBar:
    def __init__(self, target, x, y):
        self.target = target
        self.x = x
        self.y = y
        self.width = GameConfig.TILE_WIDTH * 4
        self.height = GameConfig.TILE_HEIGHT // 4

    def draw(self, screen):
        current_health_ratio = self.target.hp / GameConfig.PLAYER_START_HP
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width * current_health_ratio, self.height))


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def draw(self, screen):
        # Implement inventory drawing logic here, displaying the player's items


class UIManager:
    def __init__(self, player):
        self.player = player
        self.health_bar = HealthBar(player, 10, 10)
        self.inventory = Inventory()

    def update(self):
        # Implement any update logic for UI elements here

    def draw(self, screen):
        self.health_bar.draw(screen)
        self.inventory.draw(screen)

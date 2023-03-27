import random
import pygame
from config import GameConfig


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = GameConfig.TILE_WIDTH
        self.height = GameConfig.TILE_HEIGHT
        self.speed = random.randint(GameConfig.ENEMY_MIN_SPEED, GameConfig.ENEMY_MAX_SPEED)
        self.hp = random.randint(GameConfig.ENEMY_MIN_HP, GameConfig.ENEMY_MAX_HP)

    def move(self, game_map, player):
        # Implement enemy movement and AI logic here

    def attack(self, target):
        # Implement enemy attack logic here

    def update(self, game_map, player):
        self.move(game_map, player)
        if self.is_colliding_with(player):
            self.attack(player)

    def is_colliding_with(self, target):
        return (self.x == target.x and self.y == target.y)

    def draw(self, screen):
        pygame.draw.rect(screen, GameConfig.COLOR_ENEMY, (self.x * GameConfig.TILE_WIDTH,
                                                           self.y * GameConfig.TILE_HEIGHT,
                                                           self.width, self.height))


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def spawn_enemies(self, game_map):
        # Implement enemy spawning logic here based on the game map

    def update(self, game_map, player):
        for enemy in self.enemies:
            enemy.update(game_map, player)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

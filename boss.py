import pygame
from config import GameConfig


class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = GameConfig.TILE_WIDTH * 2
        self.height = GameConfig.TILE_HEIGHT * 2
        self.speed = GameConfig.BOSS_SPEED
        self.hp = GameConfig.BOSS_HP
        self.abilities = self.generate_abilities()
       
       
    def generate_abilities(self):
        abilities = []
        for i in range(GameConfig.BOSS_ABILITY_COUNT):
            abilities.append(random.choice(GameConfig.ABILITY_LIST))
        return abilities

    def move(self, game_map, player):
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance < GameConfig.BOSS_DETECTION_RANGE:
            dx = int(round(dx / distance))
            dy = int(round(dy / distance))

            if not game_map.is_blocked(self.x + dx, self.y + dy):
                self.x += dx
                self.y += dy

    def use_ability(self, ability, target):
        if ability == "fireball":
            # Implement fireball ability logic here
        elif ability == "freeze":
            # Implement freeze ability logic here
        # Add more abilities as needed

    

    def attack(self, target):
        # Implement boss attack logic here


    def update(self, game_map, player):
        self.move(game_map, player)
        if self.is_colliding_with(player):
            self.attack(player)

    def is_colliding_with(self, target):
        return (self.x <= target.x < self.x + self.width // GameConfig.TILE_WIDTH and
                self.y <= target.y < self.y + self.height // GameConfig.TILE_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, GameConfig.COLOR_BOSS, (self.x * GameConfig.TILE_WIDTH,
                                                         self.y * GameConfig.TILE_HEIGHT,
                                                         self.width, self.height))


class BossManager:
    def __init__(self):
        self.boss = None

    def spawn_boss(self, game_map):
        # Implement boss spawning logic here based on the game map

    def update(self, game_map, player):
        if self.boss:
            self.boss.update(game_map, player)

    def draw(self, screen):
        if self.boss:
            self.boss.draw(screen)

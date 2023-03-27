
from config import GameConfig


class Player:
    def __init__(self, x=None, y=None):
        self.x = x or GameConfig.SCREEN_WIDTH // 2
        self.y = y or GameConfig.SCREEN_HEIGHT // 2
        self.width = GameConfig.TILE_WIDTH
        self.height = GameConfig.TILE_HEIGHT
        self.speed = GameConfig.PLAYER_SPEED
        self.hp = GameConfig.PLAYER_START_HP

    def move(self, dx, dy, game_map):
        if not game_map.is_blocked(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

    def attack(self, target):
        # Implement attack logic here

    def interact(self, item):
        # Implement item interaction logic here

    def update(self):
        # Implement any update logic for the player here, such as input handling or status effects

    def draw(self, screen):
        pygame.draw.rect(screen, GameConfig.COLOR_PLAYER, (self.x * GameConfig.TILE_WIDTH,
                                                            self.y * GameConfig.TILE_HEIGHT,
                                                            self.width, self.height))

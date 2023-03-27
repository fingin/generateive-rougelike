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
        if self.item_type == "healing_potion":
            user.hp += GameConfig.HEALING_POTION_AMOUNT
        elif self.item_type == "sword":
            # Implement sword usage logic here
        elif self.item_type == "shield":
            # Implement shield usage logic here
        # Add more item types and usage logic as needed
        
    def draw(self, screen):
        pygame.draw.rect(screen, GameConfig.COLOR_ITEM, (self.x * GameConfig.TILE_WIDTH,
                                                          self.y * GameConfig.TILE_HEIGHT,
                                                          self.width, self.height))


class ItemManager:
    def __init__(self):
        self.items = []

    def spawn_items(self, game_map):
        for room in game_map.rooms:
            item_chance = random.random()
            if item_chance < GameConfig.ITEM_SPAWN_RATE:
                item_type = random_choice_index(GameConfig.ITEM_TYPES)
                x, y = room.get_random_position()
                item = Item(x, y, item_type)
                self.items.append(item)

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

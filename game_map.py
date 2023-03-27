import random
from config import GameConfig


class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class GameMap:
    def __init__(self):
        self.tiles = [[0 for _ in range(GameConfig.MAP_HEIGHT)] for _ in range(GameConfig.MAP_WIDTH)]
        self.rooms = []
        self.generate_map()

    def generate_map(self):
        for _ in range(GameConfig.MAX_ROOMS):
            width = random.randint(GameConfig.ROOM_MIN_SIZE, GameConfig.ROOM_MAX_SIZE)
            height = random.randint(GameConfig.ROOM_MIN_SIZE, GameConfig.ROOM_MAX_SIZE)
            x = random.randint(0, GameConfig.MAP_WIDTH - width - 1)
            y = random.randint(0, GameConfig.MAP_HEIGHT - height - 1)

            new_room = Room(x, y, width, height)

            if self.is_overlapping(new_room):
                continue

            self.create_room(new_room)
            self.rooms.append(new_room)

            if len(self.rooms) > 1:
                prev_room = self.rooms[-2]
                self.create_tunnel(new_room, prev_room)

    def is_overlapping(self, room):
        for other_room in self.rooms:
            if (room.x < other_room.x + other_room.width and
                    room.x + room.width > other_room.x and
                    room.y < other_room.y + other_room.height and
                    room.y + room.height > other_room.y):
                return True

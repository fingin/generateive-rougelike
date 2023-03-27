
import heapq


def random_choice_index(chances):
    return random_weighted_choice([(index, chance) for index, chance in enumerate(chances)])


def random_weighted_choice(choices):
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w
    return None


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def a_star_search(graph, start, goal):
    # Implement A* pathfinding algorithm here
    pass

# Add any other utility functions or classes needed for the project here

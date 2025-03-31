import random
import curses

# Constants
dungeon_width, dungeon_height = 40, 20
num_rooms = 5
num_enemies = 3

# Room class
class Room:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.center = (x + w // 2, y + h // 2)

    def intersects(self, other):
        return not (self.x + self.w < other.x or self.x > other.x + other.w or
                    self.y + self.h < other.y or self.y > other.y + other.h)

# Player class
class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.health = 10

    def move(self, dx, dy, dungeon):
        if dungeon[self.y + dy][self.x + dx] == '.':
            self.x += dx
            self.y += dy

# Enemy class
class Enemy:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def move_towards(self, target, dungeon):
        dx, dy = 0, 0
        if self.x < target.x:
            dx = 1
        elif self.x > target.x:
            dx = -1
        if self.y < target.y:
            dy = 1
        elif self.y > target.y:
            dy = -1
        if dungeon[self.y + dy][self.x + dx] == '.':
            self.x += dx
            self.y += dy

# Generate dungeon
def generate_dungeon():
    dungeon = [['#' for _ in range(dungeon_width)] for _ in range(dungeon_height)]
    rooms = []

    for _ in range(num_rooms):
        w, h = random.randint(5, 10), random.randint(5, 10)
        x, y = random.randint(1, dungeon_width - w - 1), random.randint(1, dungeon_height - h - 1)
        new_room = Room(x, y, w, h)

        if all(not new_room.intersects(room) for room in rooms):
            rooms.append(new_room)
            for i in range(y, y + h):
                for j in range(x, x + w):
                    dungeon[i][j] = '.'

    for i in range(len(rooms) - 1):
        x1, y1 = rooms[i].center
        x2, y2 = rooms[i + 1].center
        
        while x1 != x2:
            dungeon[y1][x1] = '.'
            x1 += 1 if x1 < x2 else -1
        while y1 != y2:
            dungeon[y1][x1] = '.'
            y1 += 1 if y1 < y2 else -1
    
    return dungeon, rooms

# Place enemies
def place_enemies(dungeon, rooms):
    enemies = []
    for _ in range(num_enemies):
        room = random.choice(rooms)
        x, y = room.center
        enemies.append(Enemy(x, y))
    return enemies

# Game loop
def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    dungeon, rooms = generate_dungeon()
    player = Player(*rooms[0].center)
    enemies = place_enemies(dungeon, rooms)
    
    while True:
        stdscr.clear()
        for y in range(dungeon_height):
            for x in range(dungeon_width):
                stdscr.addch(y, x, dungeon[y][x])
        stdscr.addch(player.y, player.x, '@')
        for enemy in enemies:
            stdscr.addch(enemy.y, enemy.x, 'E')
        stdscr.refresh()
        
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_UP:
            player.move(0, -1, dungeon)
        elif key == curses.KEY_DOWN:
            player.move(0, 1, dungeon)
        elif key == curses.KEY_LEFT:
            player.move(-1, 0, dungeon)
        elif key == curses.KEY_RIGHT:
            player.move(1, 0, dungeon)
        
        for enemy in enemies:
            enemy.move_towards(player, dungeon)
            if enemy.x == player.x and enemy.y == player.y:
                player.health -= 1
                if player.health <= 0:
                    return

if __name__ == "__main__":
    curses.wrapper(main)

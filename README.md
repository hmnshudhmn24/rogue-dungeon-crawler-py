# Rogue-like Dungeon Crawler

## Description
This is a simple rogue-like dungeon crawler written in Python using the `curses` library. The game features procedurally generated dungeons with interconnected rooms and a player that can move around using the keyboard.

## Features
- Procedurally generated dungeon layout
- Room and corridor generation
- Player movement using arrow keys
- Enemies that chase the player
- Terminal-based rendering

## Requirements
- Python 3.x
- `curses` module (built-in for Unix-based systems, may require `windows-curses` on Windows)

## Installation
### Windows:
```sh
pip install windows-curses
```

### Linux/MacOS:
No extra installation required as `curses` is built-in.

## How to Run
```sh
python rogue_dungeon.py
```

## Controls
- **Arrow Keys**: Move the player (`@`) around
- **Q**: Quit the game

## Future Enhancements
- Add combat mechanics
- Introduce loot and items
- Implement a level progression system

# Snake Game

A classic Snake game written in Python using the built-in `turtle` module.
No extra packages needed.

## How to play

- Move the snake with the **arrow keys** or **W / A / S / D**.
- Eat the red food to grow longer and earn **10 points**.
- Don't hit the walls or your own body, or the game resets.
- Your **high score** is kept until you close the game.

## Requirements

- Python 3.8 or newer
- Tkinter (included with most Python installs; on some Linux systems install it with `sudo apt install python3-tk`)

## Run the game

```bash
git clone https://github.com/itsmrbot/Snake-Game.git
cd snake-game
python snake_game.py
```

## Customize it

Open `snake_game.py` and change the values at the top:

| Setting | What it does |
| ------- | ------------ |
| `DELAY` | Time between moves. Smaller = faster snake (try `0.05`). |
| `STEP`  | How far the snake moves each turn. |
| `LIMIT` | How close to the edge the walls are. |

## How the code works

- `go_up`, `go_down`, `go_left`, `go_right` change the snake's direction.
- `move` moves the head, and `move_body` makes the body follow it.
- `add_segment` grows the snake and `move_food` places new food.
- `hit_wall` and `hit_self` check for collisions, and `game_over` resets the game.

## What you'll learn

- Functions and global variables
- Lists and loops
- Handling keyboard input
- Building a game loop with `turtle`

## Ideas to extend it

- Make the snake speed up as the score grows
- Save the high score to a file
- Add a start screen and a "Game Over" message
- Add obstacles or bonus food

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

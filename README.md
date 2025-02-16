### 2048 Game README

## Description
The 2048 game is a popular sliding block puzzle game. The objective is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. This implementation uses Python and the `tkinter` library to create an interactive and visually appealing graphical user interface (GUI) for the game.

## Features
- **Simple and Intuitive Interface**: The game features a clean and user-friendly GUI, making it easy to play and enjoy.
- **Random Tile Generation**: New tiles (either 2 or 4) are added to the board after each move.
- **Interactive Gameplay**: Players can use arrow keys to slide the tiles up, down, left, or right.
- **Dynamic Tile Merging**: Tiles with the same number merge into one when they touch.
- **Game Over Detection**: The game detects when no more moves are possible and displays a "Game Over" message.

## How to Play
1. **Start the Game**: Run the provided Python script to start the game.
2. **Move Tiles**: Use the arrow keys on your keyboard to move the tiles:
   - **Up**: Move tiles up.
   - **Down**: Move tiles down.
   - **Left**: Move tiles left.
   - **Right**: Move tiles right.
3. **Combine Tiles**: When two tiles with the same number touch, they merge into one with their combined total.
4. **Win the Game**: Keep merging tiles until you create a tile with the number 2048.
5. **Game Over**: If no more moves are possible and no empty spaces are left, the game will display a "Game Over" message.

## Installation
1. **Install Python**: Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. **Clone or Download the Repository**: Clone the repository or download the script file.
3. **Run the Script**: Execute the script using Python:
   ```sh
   python 2048-game.py
   ```

## Libraries Used
- **tkinter**: Used for creating the graphical user interface.
- **random**: Used for generating random numbers for the new tiles.

## Files
- **2048-game.py**: The main Python script file containing the game logic and GUI implementation.

Enjoy playing the 2048 game! 🎮


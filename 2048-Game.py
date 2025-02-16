import random
import tkinter as tk

def setup_gui():
    global tiles, grid_frame
    # Create the main grid frame
    grid_frame = tk.Frame(root, bg='azure3', bd=3, width=500, height=500)
    grid_frame.grid(padx=20, pady=20)
    
    # Initialize the tiles
    tiles = [[None]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            # Create individual tile frames
            frame = tk.Frame(grid_frame, bg='azure4', width=120, height=120)
            frame.grid(row=i, column=j, padx=10, pady=10)
            # Create labels for each tile
            label = tk.Label(frame, bg='azure4', font=("Helvetica", 32, "bold"), width=4, height=2)
            label.grid()
            tiles[i][j] = label
    
    # Bind key events to handle_key function
    root.bind("<Key>", handle_key)

def add_new_tile():
    # Find all empty cells
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        # Add a new tile (2 or 4) to a random empty cell
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])

def update_gui():
    # Define colors for different tile values
    colors = {0: "azure4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
              32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61", 512: "#edc850",
              1024: "#edc53f", 2048: "#edc22e"}
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            # Update the tile's text and background color
            tiles[i][j].config(text=str(value) if value != 0 else "", bg=colors[value])

def handle_key(event):
    # Map key presses to move functions
    moves = {
        'Up': move_up,
        'Down': move_down,
        'Left': move_left,
        'Right': move_right
    }
    if event.keysym in moves:
        if moves[event.keysym]():
            add_new_tile()
            update_gui()
            if not can_move():
                game_over()

def move_left():
    moved = False
    for i in range(4):
        # Extract non-zero tiles
        tiles = [board[i][j] for j in range(4) if board[i][j] != 0]
        # Merge tiles
        for k in range(len(tiles)-1):
            if tiles[k] == tiles[k+1]:
                tiles[k] *= 2
                tiles[k+1] = 0
        # Remove merged tiles and add zeros at the end
        tiles = [tile for tile in tiles if tile != 0]
        board[i] = tiles + [0]*(4-len(tiles))
        if len(tiles) != 4:
            moved = True
    return moved

def move_right():
    moved = False
    for i in range(4):
        # Extract non-zero tiles
        tiles = [board[i][j] for j in range(4) if board[i][j] != 0]
        # Merge tiles
        for k in range(len(tiles)-1, 0, -1):
            if tiles[k] == tiles[k-1]:
                tiles[k] *= 2
                tiles[k-1] = 0
        # Remove merged tiles and add zeros at the beginning
        tiles = [tile for tile in tiles if tile != 0]
        board[i] = [0]*(4-len(tiles)) + tiles
        if len(tiles) != 4:
            moved = True
    return moved

def move_up():
    global board
    # Transpose the board to reuse move_left logic
    board = [list(row) for row in zip(*board)]
    moved = move_left()
    # Transpose back to original orientation
    board = [list(row) for row in zip(*board)]
    return moved

def move_down():
    global board
    # Transpose the board to reuse move_right logic
    board = [list(row) for row in zip(*board)]
    moved = move_right()
    # Transpose back to original orientation
    board = [list(row) for row in zip(*board)]
    return moved

def can_move():
    # Check if any moves are possible
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return True
            if i < 3 and board[i][j] == board[i+1][j]:
                return True
            if j < 3 and board[i][j] == board[i][j+1]:
                return True
    return False

def game_over():
    # Unbind key events and display "Game Over"
    root.unbind("<Key>")
    for i in range(4):
        for j in range(4):
            tiles[i][j].config(bg="gray")
    tk.Label(root, text="Game Over", font=("Helvetica", 32, "bold"), fg="red").grid(row=1, column=0, columnspan=4)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("2048 Game")
    board = [[0]*4 for _ in range(4)]
    setup_gui()
    add_new_tile()
    add_new_tile()
    update_gui()
    root.mainloop()

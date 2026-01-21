# Tic-Tac-Toe Game (CLI APP) 🎮

A simple **command-line Tic-Tac-Toe game** built in **Python**, with:
- ✅ **Single Player** mode (You vs Computer)
- ✅ **Two Player** mode (Player X vs Player O)
- ✅ Easy coordinate-based moves like `A1`, `B2`, `C3`
- ✅ Menu-driven CLI with help instructions
- ✅ Win/draw detection

---

## Demo (How it Works)

- The board uses:
  - Rows: `A`, `B`, `C`
  - Columns: `1`, `2`, `3`

Example move: `B2` means **row B, column 2**.

You can also type **`exit`** during a game to return to the menu.

---

## Features

### 🎯 Game Modes
1. **Single Player**
   - You play as **X**
   - The computer plays as **O**
   - Computer chooses a random available cell

2. **Two Player**
   - Player **X** and Player **O** take turns

### 🏁 Game Rules
- Win by getting **3 in a row**:
  - Horizontal
  - Vertical
  - Diagonal
- If the board fills and no one wins → **Draw**

---

## Project Structure

```txt
.
├── tic-tac-toe.py        # Main Python game (CLI)
├── tictactoe.spec        # Spec file (used for packaging/build)
└── README.md             # Project documentation

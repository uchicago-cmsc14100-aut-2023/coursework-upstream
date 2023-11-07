from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import os.path
import board_helpers
from board import Board
from board import WON_GAME, LOST_GAME

INPUT_ERR = (
    "Invalid input. Should be exit, undo or start with m, r, or s."
    "For example, m1,2 or r1,2 or s3,0"
)
PROMPT = (
    "Enter a move (exit to quit, or ri,j to reveal, "
    "mi,j to mark, si,j to set mine. e.g. r0,1)"
)


def display_table(game_board, game_console):
    """
    Generate the table/board for rich to display

    Inputs:
        game_board (Board): the board to display
        game_console (Console): the console to display the board on
    """
    table = Table(title="Game Board", show_header=False, show_lines=True)
    for row in game_board.board:
        row_to_render = []
        for square in row:
            row_to_render.append(str(square))
        table.add_row(*row_to_render)
    game_console.print(table)
    if game_board.debug_message:
        game_console.print(f"[grey62]Debug Message: {game_board.debug_message}")


# Function to refresh the table
def refresh_table(game_board, game_console):
    """
    Refresh the display and redraw the game board

    Inputs:
        game_board (Board): the board to display
        game_console (Console): the console to display the board on
    """
    console.clear()
    display_table(game_board, game_console)


if __name__ == "__main__":
    console = Console()
    file_name = Prompt.ask(
        "Enter a file to load or i,j for a new blank board with i rows and j cols)"
    )
    if "," in file_name:
        rows, cols = file_name.split(",")
        board = Board(int(rows), int(cols))
    elif not os.path.exists(file_name):
        console.log("File does not exist.")
        exit(1)
    else:
        board = board_helpers.board_from_file(file_name)
        if board is None:
            console.log("Error reading file.")
            exit(1)
    refresh_table(board, console)

    while True:
        game_state = board.get_game_state()
        if game_state == WON_GAME:
            user_input = Prompt.ask("[bold green]You won! (exit or undo)")
        elif game_state == LOST_GAME:
            user_input = Prompt.ask("[bold magenta]You lost! (exit or undo)")
        else:
            user_input = Prompt.ask(PROMPT)
        if user_input.lower() == "exit":
            break
        if len(user_input) == 0:
            continue
        if user_input.lower() == "undo":
            board.undo_move()
        else:
            result = board_helpers.get_move(user_input)
            if result is None:
                print(INPUT_ERR)
            else:
                move, square = result
                board.play_move(move, square)

        refresh_table(board, console)

    console.print("Program exiting.")

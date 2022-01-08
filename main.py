from tkinter import *
from board.board import Board
def main() -> None:
    def fill_canvas(canvas: Canvas, board: Board) -> None:
        canvas.create_image(20, 20, anchor = NW, image = board.board_image)
        x: int = 27
        y: int = 55
        for i in range(0, 8):
            canvas.create_image(x, y, anchor = W, image = board.eighth_rank[i])
            canvas.create_image(x, y + 485, anchor = W, image = board.first_rank[i])
            x += 70
        
        
    # Generate GUI window.
    root = Tk()
    root.title("Chess 960 Randomizer/Visualzer")
    # Create board object and randomize back ranks.
    board = Board()
    board.generate_960()

    # Create canvas,
    canvas: Canvas = Canvas(root, width = 600, height = 600)
    canvas.pack()
    # Fill the canvas with pieces.
    fill_canvas(canvas, board)


    root.mainloop()

if(__name__ == "__main__"):
    main()
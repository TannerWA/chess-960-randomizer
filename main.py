"""
    Randomizes the back rank of chess pieces and provides a graphical 
    representation to the user.
    
    Copyright (C) 2022  Tanner Allen

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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

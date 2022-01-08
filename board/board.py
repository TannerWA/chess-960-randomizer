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

from random import *
from tkinter import *


class Board:
    def __init__(self) -> None:
        self.board_image: PhotoImage = PhotoImage(file = "board/board.png")

        # Place king and rooks first to ensure king is always placed between rooks.
        self.piece_order: list = ["R", "K", "R"]

        self.white_king: PhotoImage = PhotoImage(file = "pieces/white_king.png")
        self.white_queen: PhotoImage = PhotoImage(file = "pieces/white_queen.png")
        self.white_rook: PhotoImage = PhotoImage(file = "pieces/white_rook.png")
        self.white_bishop: PhotoImage = PhotoImage(file = "pieces/white_bishop.png")
        self.white_knight: PhotoImage = PhotoImage(file = "pieces/white_knight.png")

        self.black_king: PhotoImage = PhotoImage(file = "pieces/black_king.png")
        self.black_queen: PhotoImage = PhotoImage(file = "pieces/black_queen.png")
        self.black_rook: PhotoImage = PhotoImage(file = "pieces/black_rook.png")
        self.black_bishop: PhotoImage = PhotoImage(file = "pieces/black_bishop.png")
        self.black_knight: PhotoImage = PhotoImage(file = "pieces/black_knight.png")

        self.first_rank: list = [self.white_rook, self.white_king, self.white_rook]
        self.eighth_rank: list = [self.black_rook, self.black_king, self.black_rook]

    def generate_960(self) -> None:
        self.place_queen_and_knights()
        self.place_bishops()
        self.print_order()

    def place_queen_and_knights(self):
        white_list = [self.white_queen, self.white_knight, self.white_knight]
        black_list = [self.black_queen, self.black_knight, self.black_knight]
        i: int = 0
        for piece in ["Q", "N", "N"]:
            position = choice(range(len(self.piece_order) + 1))
            self.piece_order.insert(choice(range(len(self.piece_order) + 1)), piece)
            self.first_rank.insert(position, white_list[i])
            self.eighth_rank.insert(position, black_list[i])
            i += 1

    def place_bishops(self):
        bishop_position = choice(range(len(self.piece_order) + 1))
        self.piece_order.insert(bishop_position, "B")
        self.first_rank.insert(bishop_position, self.white_bishop)
        self.eighth_rank.insert(bishop_position, self.black_bishop)

        bishop_position = choice(range(bishop_position + 1, len(self.piece_order) + 1, 2))
        self.piece_order.insert(bishop_position, "B")
        self.first_rank.insert(bishop_position, self.white_bishop)
        self.eighth_rank.insert(bishop_position, self.black_bishop)

    def print_order(self) -> None:
        print(self.piece_order)
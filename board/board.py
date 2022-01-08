from tkinter import *
from random import *
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

        self.first_rank: list = []
        self.eighth_rank: list = []

    def generate_960(self) -> None:
        self.place_queen_and_knights()
        self.place_bishops()
        self.print_order()
        self.order_images()

    def place_queen_and_knights(self):
        for piece in ["Q", "N", "N"]:
            self.piece_order.insert(choice(range(len(self.piece_order) + 1)), piece)

    def place_bishops(self):
        bishop_position = choice(range(len(self.piece_order) + 1))
        self.piece_order.insert(bishop_position, "B")
        self.piece_order.insert(choice(range(bishop_position + 1, len(self.piece_order) + 1, 2)), "B")

    def print_order(self) -> None:
        print(self.piece_order)

    def order_images(self) -> None:
        for piece in self.piece_order:
            if(piece == "K"):
                self.first_rank.append(self.white_king)
                self.eighth_rank.append(self.black_king)
            elif(piece == "Q"):
                self.first_rank.append(self.white_queen)
                self.eighth_rank.append(self.black_queen)
            elif(piece == "R"):
                self.first_rank.append(self.white_rook)
                self.eighth_rank.append(self.black_rook)
            elif(piece == "B"):
                self.first_rank.append(self.white_bishop)
                self.eighth_rank.append(self.black_bishop)
            elif(piece == "N"):
                self.first_rank.append(self.white_knight)
                self.eighth_rank.append(self.black_knight)

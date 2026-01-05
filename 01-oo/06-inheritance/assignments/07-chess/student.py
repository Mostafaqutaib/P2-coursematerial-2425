from abc import ABC, abstractmethod

class Board(ABC):
    def __init__(self, size):
        self.size = size
        self.board = self.create_board()

    @abstractmethod
    def create_board(self):
        pass

    def is_inside(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size


class ChessBoard(Board):
    def __init__(self):
        super().__init__(8)

    def create_board(self):
        board = []
        for row in range(self.size):
            board_row = []
            for col in range(self.size):
                board_row.append("W" if (row + col) % 2 == 0 else "B")
            board.append(board_row)
        return board

    def color_at(self, row, col):
        if not self.is_inside(row, col):
            raise ValueError("Invalid position")
        return self.board[row][col]

    def print_board(self):
        for row in self.board:
            print(" ".join(row))


class Position:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def move(self, dx, dy):
        return Position(self.x + dx, self.y + dy)

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class ChessPiece:
    def __init__(self, position, color):
        if not ChessPiece.is_valid_position(position):
            raise ValueError("invalid position")
        if not ChessPiece.is_valid_color(color):
            raise ValueError("invalid color")
        self.__position = position
        self.__color = color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        if not ChessPiece.is_valid_position(new_position):
            raise ValueError("invalid position")
        self.__position = new_position

    @property
    def color(self):
        return self.__color

    @staticmethod
    def is_valid_color(color):
        return color in ["black", "white"]

    @staticmethod
    def is_valid_position(position):
        return 0 <= position.x < 8 and 0 <= position.y < 8
    


class Pawn(ChessPiece):
    def is_legal_move(self, new_position):
        if not ChessPiece.is_valid_position(new_position):
            return False
        direction = 1 if self.color == "white" else -1
        return self.position.move(0, direction) == new_position

    def move(self, new_position):
        if not self.is_legal_move(new_position):
            raise ValueError("illegal move")
        self.position = new_position


class King(ChessPiece):
    def is_legal_move(self, new_position):
        if new_position == self.position:
            return False
        if not ChessPiece.is_valid_position(new_position):
            return False
        if abs(new_position.x - self.position.x) > 1:
            return False
        if abs(new_position.y - self.position.y) > 1:
            return False
        return True

    def move(self, new_position):
        if not self.is_legal_move(new_position):
            raise ValueError("illegal move")
        self.position = new_position

class Knight(ChessPiece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def is_legal_move(self, new_position):
        if not ChessPiece.is_valid_position(new_position):
            return False
        if new_position == self.position:
            return False
        direction = 1 if self.color == "white" else -1
        return self.position.move(0, direction) == new_position
    def possible_moves(self):
        



p = Pawn(Position(0, 1), "white")
print(p.is_legal_move(Position(0, 2)))  # True حسب direction=+1

k = King(Position(4, 4), "black")
print(k.is_legal_move(Position(5, 5)))  # True
print(k.is_legal_move(Position(6, 6)))  # False
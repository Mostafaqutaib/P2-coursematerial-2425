board = []
        for r in self.__board_size:
            board_row = []
            for col in self.__board_size:
                if (r + col) % 2 == 0:
                    board_row.append("w")
                else:
                    board_row.append("B")
            board.append(board_row)
        return boardboard = []
        for r in self.__board_size:
            board_row = []
            for col in self.__board_size:
                if (r + col) % 2 == 0:
                    board_row.append("w")
                else:
                    board_row.append("B")
            board.append(board_row)
        return board
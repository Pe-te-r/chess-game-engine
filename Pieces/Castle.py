from Pieces import Piece


class Castle(Piece):
    def __init__(self, color, name='rook', value=5):
        super().__init__(color, name, value)

    def valid_moves(self, row, col, squares):
        valid_moves = []

        # Check moves in the same row
        for i in range(1, 8):
            if row + i < 8:
                square = squares[row + i][col]
                if square.is_empty():
                    valid_moves.append((row + i, col))
                elif square.piece.color != self.color:
                    valid_moves.append((row + i, col))
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if row - i >= 0:
                square = squares[row - i][col]
                if square.is_empty():
                    valid_moves.append((row - i, col))
                elif square.piece.color != self.color:
                    valid_moves.append((row - i, col))
                    break
                else:
                    break
            else:
                break

        # Check moves in the same column
        for i in range(1, 8):
            if col + i < 8:
                square = squares[row][col + i]
                if square.is_empty():
                    valid_moves.append((row, col + i))
                elif square.piece.color != self.color:
                    valid_moves.append((row, col + i))
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            if col - i >= 0:
                square = squares[row][col - i]
                if square.is_empty():
                    valid_moves.append((row, col - i))
                elif square.piece.color != self.color:
                    valid_moves.append((row, col - i))
                    break
                else:
                    break
            else:
                break

        return valid_moves
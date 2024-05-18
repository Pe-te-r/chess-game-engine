from Pieces import Piece

class Queen(Piece):
    def __init__(self, color, name='queen', value=8):
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

        # Generate bishop moves (diagonal)
        deltas = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        for dr, dc in deltas:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                square = squares[r][c]
                if square.is_empty() or square.piece.color != self.color:
                    valid_moves.append((r, c))
                    if not square.is_empty():
                        break
                else:
                    break
                r += dr
                c += dc

        return valid_moves
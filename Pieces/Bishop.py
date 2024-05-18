from Pieces import Piece


class Bishop(Piece):
    def __init__(self, color, name='bishop', value=3):
        super().__init__(color, name, value)

    def valid_moves(self, row,col, squares):
        moves=[]
        deltas = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        for dr, dc in deltas:
            r,c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                square = squares[r][c]
                if square.is_empty() or square.piece.color != self.color:
                    moves.append((r, c))
                    if not square.is_empty():
                        break
                else:
                    break
                r += dr
                c += dc
        
        return moves
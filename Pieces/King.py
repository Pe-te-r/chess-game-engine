from Pieces import Piece

class King(Piece):
    def __init__(self,color,name='king',value=10):
        super().__init__(color,name,value)

    def valid_moves(self,row,col,squares):
        valid_moves=[(row+1,col),(row-1,col),(row,col+1),(row,col-1),(row-1,col-1),(row+1,col+1),(row+1,col-1),(row-1,col+1)]
        # opponent_king_positions = self.get_opponent_king_positions(row, col, squares)
        filtered_moves = []
        for move in valid_moves:
            r, c = move
            if 0 <= r < 8 and 0 <= c < 8:
                check_square=squares[move[0]][move[1]]
                if check_square.is_empty() or check_square.piece.color != self.color:
                    filtered_moves.append(move)
        return filtered_moves

    def get_opponent_king_positions(self, row, col, squares):
        opponent_king_positions = []
        for i in range(max(0, row - 1), min(8, row + 2)):
            for j in range(max(0, col - 1), min(8, col + 2)):
                if not (i == row and j == col):  # Exclude the king's own square
                    square = squares[i][j]
                    if not square.is_empty() and square.piece.color != self.color and square.piece.name == 'king':
                        opponent_king_positions.append((i, j))
        return opponent_king_positions
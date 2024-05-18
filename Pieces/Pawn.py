from Pieces import Piece

class Pawn(Piece):
    def __init__(self, color, name='pawn', value=1):
        super().__init__(color, name, value)

    def valid_moves(self, row, col, squares):
        valid_squares = []

        # Define the direction of movement based on the pawn's color
        direction = 1 if self.color == 'white' else -1

        # Check if the square in front of the pawn is empty
        if squares[row][col + direction].is_empty():
            valid_squares.append((row, col + direction))

            # Check for the initial double move
            if (col == 1 and self.color == 'white') or (col == 6 and self.color == 'black'):
                if squares[row][col + 2 * direction].is_empty():
                    valid_squares.append((row, col + 2 * direction))

        # Check for capturing diagonally
        for dcol in [-1, 1]:
            if 0 <= row + dcol < 8:
                target_square = squares[row + dcol][col + direction]
                if not target_square.is_empty() and target_square.piece.color != self.color:
                    valid_squares.append((row + dcol, col + direction))

        return valid_squares

        

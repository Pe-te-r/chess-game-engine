from Pieces import Piece

class Knight(Piece):
    def __init__(self,color,name='knight',value=4):
        super().__init__(color,name,value)

    def valid_moves(self,row,col,squares):
        valid_squares=[
            (row+1,col+2),
            (row+2,col+1),
            (row-1,col-2),
            (row-2,col-1),
            (row+1,col-2),
            (row+2,col-1),
            (row-1,col+2),
            (row-2,col+1)
            ]
        return valid_squares

import java.awt.Color;

public class Pawn implements Piece {
    private Color color;
    private int row;
    private int col;
    // flag to track whether the pawn has made its first move or not
    private boolean hasMoved;

    public Pawn(Color color, int row, int col) {
        this.color = color;
        this.row = row;
        this.col = col;
        // Initialized hasMoved to false when the pawn is created
        this.hasMoved = false;
    }
    @Override
    public boolean isValidMove(int newRow, int newCol, Chessboard board) {
        // Implement rules for pawn movement and capture

        // Calculate row and column differences
        int rowDiff = newRow - row;
        int colDiff = newCol - col;

        // Ensure ending square is within board bounds
        if (newRow < 0 || newRow > 7 || newCol < 0 || newCol > 7) {
            return false;
        }

        // White pawn moves one square forward
        if (color == Color.BLACK) {
            if (rowDiff == -1 && colDiff == 0) {
                hasMoved = true;
                // Normal move, one square forward
                return !board.isOccupied(newRow, newCol);
            } else if (rowDiff == -2 && colDiff == 0 && !hasMoved) {
                hasMoved = true;
                // First move, can move two squares forward
                return !board.isOccupied(newRow, newCol) && !board.isOccupied(newRow + 1, newCol);
            } else if (rowDiff == -1 && Math.abs(colDiff) == 1) {
                hasMoved = true;
                // Capture move, one square diagonally forward
                return board.isOccupied(newRow, newCol) && board.getPiece(newRow, newCol).getColor() != color;
            }
        }
        // Black pawn moves one square forward
        else if (color == Color.WHITE) {
            if (rowDiff == 1 && colDiff == 0) {
                hasMoved = true;
                // Normal move, one square forward
                return !board.isOccupied(newRow, newCol);
            } else if (rowDiff == 2 && colDiff == 0 && !hasMoved) {
                hasMoved = true;
                // First move, can move two squares forward
                return !board.isOccupied(newRow, newCol) && !board.isOccupied(newRow - 1, newCol);
            } else if (rowDiff == 1 && Math.abs(colDiff) == 1) {
                hasMoved = true;
                // Capture move, one square diagonally forward
                return board.isOccupied(newRow, newCol) && board.getPiece(newRow, newCol).getColor() != color;
            }
        }
        // Invalid move
        return false;
    }

    @Override
    public Color getColor() {
        return color;
    }

    @Override
    public char getSymbol() {
        return 'P';
    }
}

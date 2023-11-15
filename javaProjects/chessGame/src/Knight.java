import java.awt.Color;

public class Knight implements Piece {
    private Color color;
    private int row;
    private int col;

    public Knight (Color color, int row, int col) {
        this.color = color;
        this.row = row;
        this.col = col;
    }

    @Override
    public boolean isValidMove(int newRow, int newCol, Chessboard board) {
        // Implement rules for knight movement and capture

        // Calculate row and column differences
        int rowDiff = Math.abs(newRow - row);
        int colDiff = Math.abs(newCol - col);

        // Ensure ending square is in bounds
        if (newRow < 0 || newRow > 7 || newCol < 0 || newCol > 7) {
            return false;
        }

        // Knights move in an L-shape (two squares in one direction and one square in the other
        // There are eight possible valid knight moves
        if ((rowDiff == 2 && colDiff == 1) || (rowDiff == 1 && colDiff == 2)) {
            // Check if the ending square is unoccupied or contains an enemy piece
            if (!board.isOccupied(newRow, newCol) || board.getPiece(newRow, newCol).getColor() != color) {
                // Valid move
                return true;
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
        return 'N';
    }
}

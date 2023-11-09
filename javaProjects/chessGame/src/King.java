import java.awt.Color;

public class King implements Piece {
    private Color color;
    private int row;
    private int col;

    public King(Color color, int row, int col) {
        this.color = color;
        this.row = row;
        this.col = col;
    }

    @Override
    public boolean isValidMove(int newRow, int newCol, Chessboard board) {
        // Implement rules for King movement and capture

        // Calculate row column differences
        int rowDiff = Math.abs(newRow - row);
        int colDiff = Math.abs(newCol - col);

        // Ensure the destination square is within the chessboard
        if (newRow < 0 || newRow > 7 || newCol < 0 || newCol > 7) {
            return false;
        }

        // The king can move in any direction, but only one square at a time.
        if ((rowDiff == 1 && colDiff == 0) || (rowDiff == 0 && colDiff == 1) || (rowDiff == 1 && colDiff == 1)) {
            // Check if ending square is unoccupied or contains an enemy piece
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
}


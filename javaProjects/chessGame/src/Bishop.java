import java.awt.Color;

public class Bishop implements Piece {
    private Color color;
    private int row;
    private int col;

    public Bishop(Color color, int row, int col) {
        this.color = color;
        this.row = row;
        this.col = col;
    }

    @Override
    public boolean isValidMove(int newRow, int newCol, Chessboard board) {
        // Implement rules for bishop movement and capture

        // Calculate row and column differences
        int rowDiff = newRow - row;
        int colDiff = newCol - col;

        // Ensure the ending square is in bounds
        if (newRow < 0 || newRow > 7 || newCol < 0 || newCol > 7) {
            return false;
        }

        // Bishop moves diagonally
        // Can move in any direction as long as there are no obstructions
        if (Math.abs(rowDiff) == Math.abs(colDiff)) {
            // Determine the direction of movement for rows
            int rowStep = (rowDiff > 0) ? 1 : -1;
            // Determine the direction of movement for columns
            int colStep = (colDiff > 0) ? 1 : -1;

            int currentRow = row + rowStep;
            int currentCol = col + colStep;

            // Check if there are obstructions along the diagonal path
            while (currentRow != newRow && currentCol != newCol) {
                if (board.isOccupied(currentRow, currentCol)) {
                    // Path is obstructed
                    return false;
                }
                currentRow += rowStep;
                currentCol += colStep;
            }

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
}


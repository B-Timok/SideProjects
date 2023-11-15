import java.awt.Color;

public class Rook implements Piece {
    private Color color;
    private int row;
    private int col;

    public Rook(Color color, int row, int col) {
        this.color = color;
        this.row = row;
        this.col = col;
    }

    @Override
    public boolean isValidMove(int newRow, int newCol, Chessboard board) {
        // Implement rules for Rook movement and capture

        // Calculate row column differences
        int rowDiff = newRow - row;
        int colDiff = newCol - col;

        // Ensure the ending square is in bounds
        if (newRow < 0 || newRow > 7 || newCol < 0 || newCol > 7) {
            return false;
        }

        // Rook moves horizontally and vertically
        // Can move in either direction as long as there are no obstructions
        if ((rowDiff == 0 && colDiff != 0) || (rowDiff != 0 && colDiff == 0)) {
            int step = (rowDiff == 0) ? Integer.signum(colDiff) : Integer.signum(rowDiff);

            int currentRow = row + step;
            int currentCol = col + step;

            // Check if there are any obstructions along the path
            while (currentRow != newRow || currentCol != newCol) {
                if (board.isOccupied(currentRow, currentCol)) {
                    // Path is obstructed
                    return false;
                }
                currentRow += (rowDiff == 0) ? 0 : step;
                currentCol += (colDiff == 0) ? 0 : step;
            }

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

    @Override
    public char getSymbol() {
        return 'R';
    }
}

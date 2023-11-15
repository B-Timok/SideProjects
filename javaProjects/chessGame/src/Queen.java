import java.awt.Color;

public class Queen implements Piece {
    private Color color;
    private int row;
    private int col;

    public Queen(Color color, int row, int col) {
        this.color = color;
        this.row = row;
        this.col = col;
    }

    @Override
    public boolean isValidMove(int newRow, int newCol, Chessboard board) {
        // Implement rules for Queen movement and capture

        // Calculate row column differences
        int rowDiff = newRow - row;
        int colDiff = newCol - col;

        // Ensure the ending square is in bounds
        if (newRow < 0 || newRow > 7 || newCol < 0 || newCol > 7) {
            return false;
        }

        // The queen combines the rook and bishop movements (horizontally, vertically, and diagonally)
        if ((rowDiff == 0 && colDiff != 0) || (rowDiff != 0 && colDiff == 0)) {
            // Rook-like movement (horizontal and vertical)
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
        } else if (Math.abs(rowDiff) == Math.abs(colDiff)) {
            // Bishop-like movement (diagonal)
            int rowStep = (rowDiff > 0) ? 1 : -1;
            int colStep = (colDiff > 0) ? 1 : -1;

            int currentRow = row + rowStep;
            int currentCol = col + colStep;

            // Check if there are any obstructions along the path
            while (currentRow != newRow && currentCol != newCol) {
                if (board.isOccupied(currentRow, currentCol)) {
                    // Path is obstructed
                    return false;
                }
                currentRow += rowStep;
                currentCol += colStep;
            }
        } else {
            // Invalid move
            return false;
        }

        // Check if ending square is unoccupied or contains an enemy piece
        if (!board.isOccupied(newRow, newCol) || board.getPiece(newRow, newCol).getColor() != color) {
            // Valid move
            return true;
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
        return 'Q';
    }
}

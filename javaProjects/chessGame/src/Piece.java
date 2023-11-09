import java.awt.Color;

public interface Piece {
    boolean isValidMove(int newRow, int newCol, Chessboard board);
    Color getColor();
}

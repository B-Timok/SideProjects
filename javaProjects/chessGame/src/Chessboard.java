import java.awt.Color;

public class Chessboard {
    private Piece[][] board;

    public Chessboard() {
        board = new Piece[8][8];
        initializeBoard();
    }

    public void initializeBoard() {
        initializeSide(Color.WHITE, 0);
        initializeSide(Color.BLACK, 7);
    }

    private void initializeSide(Color color, int row) {
        board[row][0] = new Rook(color, row, 0);
        board[row][1] = new Knight(color, row, 1);
        board[row][2] = new Bishop(color, row, 2);
        board[row][3] = new Queen(color, row, 3);
        board[row][4] = new King(color, row, 4);
        board[row][5] = new Bishop(color, row, 5);
        board[row][6] = new Knight(color, row, 6);
        board[row][7] = new Rook(color, row, 7);

        int pawnRow = (color == Color.WHITE) ? row + 1 : row - 1;
        for (int col = 0; col < 8; col++) {
            board[pawnRow][col] = new Pawn(color, pawnRow, col);
        }
    }

    public Piece movePiece(int fromRow, int fromCol, int toRow, int toCol) {
        // Check if the move is valid for the piece at (fromRow, fromCol)
        if (board[fromRow][fromCol].isValidMove(toRow, toCol, this)) {
            // Save the piece at the destination (toRow, toCol) for undoing the move
            Piece pieceAtDestination = board[toRow][toCol];

            // Move the piece to the new location
            board[toRow][toCol] = board[fromRow][fromCol];
            board[fromRow][fromCol] = null;

            // Return the piece that was moved
            return board[toRow][toCol];
        }

        // Invalid move, return null
        return null;
    }


    public void undoMove(int fromRow, int fromCol, int toRow, int toCol) {
        // Swap the pieces back to their original positions
        Piece pieceFrom = board[toRow][toCol];
        Piece pieceTo = board[fromRow][fromCol];

        board[fromRow][fromCol] = pieceFrom;
        board[toRow][toCol] = pieceTo;
    }

    public boolean isKingInCheck(Color kingColor) {
        // Find the position of the king
        int kingRow = -1;
        int kingCol = -1;

        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                Piece piece = board[row][col];
                if ((piece instanceof King) && (piece.getColor() == kingColor)) {
                    kingRow = row;
                    kingCol = col;
                    break;
                }
            }
        }

        if (kingRow == -1 || kingCol == -1) {
            // King not found, something wrong
            return false;
        }

        // Check if any opponent pieces can capture the king
        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                Piece piece = board[row][col];
                if (piece != null && piece.getColor() != kingColor) {
                    // Check if the opponent's piece can capture the king
                    if (piece.isValidMove(kingRow, kingCol, this)) {
                        // King is in check
                        return true;
                    }
                }
            }
        }

        // King is not check
        return false;
    }

    private boolean canKingEscapeCheck(Color kingColor) {
        int kingRow = -1;
        int kingCol = -1;

        // Find the position of the king
        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                Piece piece = board[row][col];
                if (piece instanceof King && piece.getColor() == kingColor) {
                    kingRow = row;
                    kingCol = col;
                    break;
                }
            }
        }

        if (kingRow == -1 || kingCol == -1) {
            // King not found, something wrong
            return false;
        }

        // Check all possible moves of the king
        for (int newRow = 0; newRow < 8; newRow++) {
            for (int newCol = 0; newCol < 8; newCol++) {
                if (board[kingRow][kingCol].isValidMove(newRow, newCol, this)) {
                    // Simulate the move
                    Piece originalPiece = board[newRow][newCol];
                    board[newRow][newCol] = board[kingRow][kingCol];
                    board[kingRow][kingCol] = null;

                    // Check if the king is still in check after the move
                    if (!isKingInCheck(kingColor)) {
                        // Undo the move
                        board[kingRow][kingCol] = board[newRow][newCol];
                        board[newRow][newCol] = originalPiece;
                        // King can escape check
                        return true;
                    }

                    // Undo the move
                    board[kingRow][kingCol] = board[newRow][newCol];
                    board[newRow][newCol] = originalPiece;
                }
            }
        }

        // King cannot escape check
        return false;
    }

    private boolean canAnyPieceBlockCheck(Color kingColor) {
        // Iterate over all pieces on the board
        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                Piece piece = board[row][col];

                // Check if the piece belongs to the same color as the king
                if (piece != null && piece.getColor() == kingColor) {
                    // Iterate over all possible moves of the piece
                    for (int newRow = 0; newRow < 8; newRow++) {
                        for (int newCol = 0; newCol < 8; newCol++) {
                            if (piece.isValidMove(newRow, newCol, this)) {
                                // Simulate the move
                                Piece originalPiece = board[newRow][newCol];
                                board[newRow][newCol] = piece;
                                board[row][col] = null;

                                // Check if the king is still in check after the move
                                if (!isKingInCheck(kingColor)) {
                                    // Undo the move
                                    board[row][col] = board[newRow][newCol];
                                    board[newRow][newCol] = originalPiece;
                                    // Piece can block the threat
                                    return true;
                                }

                                // Undo the move
                                board[row][col] = board[newRow][newCol];
                                board[newRow][newCol] = originalPiece;
                            }
                        }
                    }
                }
            }
        }

        // No piece can block the threat
        return false;
    }

    public boolean isCheckmate(Color kingColor) {
        // Check if the king is in checkmate
        if (isKingInCheck(kingColor)) {
            // King is not in check, not in checkmate
            return false;
        }

        // Check if the king can move to a safe square
        if (canKingEscapeCheck(kingColor)) {
            // King can escape check
            return false;
        }

        // Check if any other pieces can block the threat
        if (canAnyPieceBlockCheck(kingColor)) {
            // Another piece can block the threat
            return false;
        }

        // If neither condition is met, it's checkmate
        return true;
    }

    public boolean isOccupied(int row, int col) {
        if (row < 0 || row > 7 || col < 0 || col > 7) {
            // Out of bounds, not occupied
            return false;
        }
        // Check if square is occupied by a piece
        return board[row][col] != null;
    }

    public Piece getPiece(int row, int col) {
        if (row < 0 || row > 7 || col < 0 || col > 7) {
            // Square is out of bounds
            return null;
        }
        return board[row][col];
    }
}

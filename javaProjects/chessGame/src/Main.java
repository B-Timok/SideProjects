// The start to a beautiful game of chess.

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Create a new chessboard
        Chessboard chessboard = new Chessboard();

        // Print the initial chessboard
        printChessboard(chessboard);

        // Create a Scanner to read user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user for moves until they enter a specific command (e.g., "exit")
        while (true) {
            System.out.println("Enter your move in standard chess notation (e.g., e2e4), or type 'exit' to end the game:");
            String userInput = scanner.nextLine();

            // Check if the user wants to exit
            if (userInput.equalsIgnoreCase("exit")) {
                System.out.println("Game over. Exiting...");
                break;
            }

            // Process the user's move
            try {
                processMove(userInput, chessboard);
            } catch (IllegalArgumentException e) {
                System.out.println("Invalid move. Please try again.");
                continue; // Restart the loop to prompt the user for another move
            }

            // Print the chessboard after the move
            printChessboard(chessboard);
        }

        // Close the scanner
        scanner.close();
    }

    // Helper method to process the user's move
    private static void processMove(String move, Chessboard chessboard) {
        // Check for "exit" command
        if (move.equalsIgnoreCase("exit")) {
            System.out.println("Game over. Exiting...");
            // Terminate the program
            System.exit(0);
        }

        // Check if the input has at least four characters
        if (move.length() < 4) {
            throw new IllegalArgumentException("Invalid move format. Please enter a valid move.");
        }

        // Parse the move and convert it to row and column indices
        int startCol = move.charAt(0) - 'a';
        int startRow = Character.getNumericValue(move.charAt(1)) - 1;
        int endCol = move.charAt(2) - 'a';
        int endRow = Character.getNumericValue(move.charAt(3)) - 1;

        // Make the move on the chessboard
        chessboard.movePiece(startRow, startCol, endRow, endCol);
    }


    // Helper method to print the chessboard
    private static void printChessboard(Chessboard chessboard) {
        for (int row = 7; row >= 0; row--) {
            System.out.print(row + 1 + " ");
            for (int col = 0; col < 8; col++) {
                Piece piece = chessboard.getPiece(row, col);
                if (piece == null) {
                    System.out.print("- ");
                } else {
                    // Assuming each piece has a one-character representation
                    System.out.print(piece.getSymbol() + " ");
                }
            }
            System.out.println();
        }
        System.out.println("  a b c d e f g h");
        System.out.println();
    }
}

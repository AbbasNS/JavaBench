package pa1.model;

public class GameState {

    public static final int UNLIMITED_LIVES = -1;

    private final GameBoard gameBoard;

    private final MoveStack moveStack = new MoveStack();

    private int numDeaths = 0;

    private int numMoves = 0;

    private int numLives;

    private final int initialNumOfGems;

    public GameState(final GameBoard gameBoard) {
    }

    public GameState(final GameBoard gameBoard, final int numLives) {
    }

    public boolean hasWon() {
    }

    public boolean hasLost() {
    }

    public int increaseNumLives(final int delta) {
    }

    public int decreaseNumLives(final int delta) {
    }

    public int decrementNumLives() {
    }

    public int incrementNumMoves() {
    }

    public int incrementNumDeaths() {
    }

    public int getNumDeaths() {
    }

    public int getNumMoves() {
    }

    public boolean hasUnlimitedLives() {
    }

    public int getNumLives() {
    }

    public int getNumGems() {
    }

    public int getScore() {
    }

    public GameBoardController getGameBoardController() {
    }

    public GameBoardView getGameBoardView() {
    }

    public GameBoard getGameBoard() {
    }

    public MoveStack getMoveStack() {
    }
}

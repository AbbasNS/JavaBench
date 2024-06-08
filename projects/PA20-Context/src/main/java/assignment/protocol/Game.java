package assignment.protocol;

public abstract class Game implements Cloneable {

    protected Configuration configuration;

    protected Piece[][] board;

    protected Player currentPlayer;

    protected int numMoves = 0;

    public Game(Configuration configuration) {
    }

    public abstract Player start() {
    }

    public abstract Player getWinner(Player lastPlayer, Piece lastPiece, Move lastMove) {
    }

    public abstract void updateScore(Player player, Piece piece, Move move) {
    }

    public abstract void movePiece(Move move) {
    }

    public abstract Move[] getAvailableMoves(Player player) {
    }

    public void refreshOutput() {
    }

    public Piece getPiece(Place place) {
    }

    public Piece getPiece(int x, int y) {
    }

    public Player getCurrentPlayer() {
    }

    public Player[] getPlayers() {
    }

    public int getNumMoves() {
    }

    public Configuration getConfiguration() {
    }

    public Place getCentralPlace() {
    }

    @Override
    public Game clone() throws CloneNotSupportedException {
    }
}

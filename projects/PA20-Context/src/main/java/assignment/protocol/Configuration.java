package assignment.protocol;

public class Configuration implements Cloneable {

    private final int size;

    private Player[] players;

    private Piece[][] initialBoard;

    private Place centralPlace;

    private final int numMovesProtection;

    public Configuration(int size, Player[] players, int numMovesProtection) {
    }

    public Configuration(int size, Player[] players) {
    }

    public void addInitialPiece(Piece piece, Place place) {
    }

    public void addInitialPiece(Piece piece, int x, int y) {
    }

    public int getSize() {
    }

    public Player[] getPlayers() {
    }

    public Piece[][] getInitialBoard() {
    }

    public Place getCentralPlace() {
    }

    public int getNumMovesProtection() {
    }

    @Override
    public Configuration clone() throws CloneNotSupportedException {
    }
}

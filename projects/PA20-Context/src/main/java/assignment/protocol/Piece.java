package assignment.protocol;

public abstract class Piece {

    private final Player player;

    public Piece(Player player) {
    }

    public final Player getPlayer() {
    }

    public abstract char getLabel() {
    }

    public abstract Move[] getAvailableMoves(Game game, Place source) {
    }
}

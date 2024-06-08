package assignment.protocol;

public abstract class Player implements Cloneable {

    protected final String name;

    protected int score;

    protected final Color color;

    public Player(String name, Color color) {
    }

    @Override
    public boolean equals(Object o) {
    }

    @Override
    public int hashCode() {
    }

    public final String getName() {
    }

    public final int getScore() {
    }

    public final void setScore(int score) {
    }

    public String toString() {
    }

    public final Color getColor() {
    }

    @Override
    public Player clone() throws CloneNotSupportedException {
    }

    public abstract Move nextMove(Game game, Move[] availableMoves) {
    }
}

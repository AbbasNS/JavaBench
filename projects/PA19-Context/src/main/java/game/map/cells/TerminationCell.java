package game.map.cells;

public class TerminationCell extends Cell {

    private boolean isFilled = false;

    public final Direction pointingTo;

    public final Type type;

    public TerminationCell(Coordinate coord, Direction direction, Type type) {
    }

    public void setFilled() {
    }

    @Override
    public char toSingleChar() {
    }

    public enum Type {

        SOURCE, SINK
    }

    public static class CreateInfo {

        public final Coordinate coord;

        public final Direction dir;

        public CreateInfo(Coordinate coord, Direction dir) {
        }
    }
}

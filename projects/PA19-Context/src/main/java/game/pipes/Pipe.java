package game.pipes;

public class Pipe implements MapElement {

    private final Shape shape;

    private boolean filled = false;

    public Pipe(Shape shape) {
    }

    public void setFilled() {
    }

    public boolean getFilled() {
    }

    public Direction[] getConnections() {
    }

    @Override
    public char toSingleChar() {
    }

    public static Pipe fromString(String rep) {
    }

    public enum Shape {

        HORIZONTAL(PipePatterns.Filled.HORIZONTAL, PipePatterns.Unfilled.HORIZONTAL),
        VERTICAL(PipePatterns.Filled.VERTICAL, PipePatterns.Unfilled.VERTICAL),
        TOP_LEFT(PipePatterns.Filled.TOP_LEFT, PipePatterns.Unfilled.TOP_LEFT),
        TOP_RIGHT(PipePatterns.Filled.TOP_RIGHT, PipePatterns.Unfilled.TOP_RIGHT),
        BOTTOM_LEFT(PipePatterns.Filled.BOTTOM_LEFT, PipePatterns.Unfilled.BOTTOM_LEFT),
        BOTTOM_RIGHT(PipePatterns.Filled.BOTTOM_RIGHT, PipePatterns.Unfilled.BOTTOM_RIGHT),
        CROSS(PipePatterns.Filled.CROSS, PipePatterns.Unfilled.CROSS);

        final char filledChar;

        final char unfilledChar;

        Shape(char filled, char unfilled) {
        }

        char getCharByState(boolean isFilled) {
        }
    }
}

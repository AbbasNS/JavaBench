package game.map.cells;

public abstract class Cell implements MapElement {

    public final Coordinate coord;

    Cell(Coordinate coord) {
    }

    public static Cell fromChar(char c, Coordinate coord, TerminationCell.Type terminationType) {
    }
}

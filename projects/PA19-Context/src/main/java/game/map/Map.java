package game.map;

public class Map {

    private final int rows;

    private final int cols;

    public final Cell[][] cells;

    private TerminationCell sourceCell;

    private TerminationCell sinkCell;

    private final Set<Coordinate> filledTiles = new HashSet<>();

    private int prevFilledTiles = 0;

    private Integer prevFilledDistance;

    public Map(int rows, int cols) {
    }

    public Map(int rows, int cols, Cell[][] cells) {
    }

    static Map fromString(int rows, int cols, String cellsRep) {
    }

    public boolean tryPlacePipe(final Coordinate coord, final Pipe pipe) {
    }

    boolean tryPlacePipe(int row, int col, Pipe p) {
    }

    public void display() {
    }

    public void undo(final Coordinate coord) {
    }

    public void fillBeginTile() {
    }

    public void fillTiles(int distance) {
    }

    public boolean checkPath() {
    }

    public boolean hasLost() {
    }
}

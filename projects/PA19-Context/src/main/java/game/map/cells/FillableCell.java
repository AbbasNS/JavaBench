package game.map.cells;

public class FillableCell extends Cell implements MapElement {

    private Pipe pipe;

    public FillableCell(Coordinate coord) {
    }

    public FillableCell(Coordinate coord, Pipe pipe) {
    }

    public Optional<Pipe> getPipe() {
    }

    @Override
    public char toSingleChar() {
    }

    public void setPipe(Pipe pipe) {
    }
}

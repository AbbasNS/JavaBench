package game;

public class Game {

    private final Map map;

    private final PipeQueue pipeQueue;

    private final DelayBar delayBar;

    private final CellStack cellStack = new CellStack();

    private int numOfSteps = 0;

    public Game(int rows, int cols) {
    }

    public Game(int rows, int cols, int delay, Cell[][] cells, List<Pipe> pipes) {
    }

    static Game fromString(int rows, int cols, int delay, String cellsRep, List<Pipe> pipes) {
    }

    public boolean placePipe(int row, char col) {
    }

    public void skipPipe() {
    }

    public boolean undoStep() {
    }

    public void display() {
    }

    public void updateState() {
    }

    public boolean hasWon() {
    }

    public boolean hasLost() {
    }

    public int getNumOfSteps() {
    }
}

package pa1.util;

import pa1.model.Cell;
import pa1.model.GameBoard;
import pa1.model.Position;

import java.util.function.Function;

public class GameBoardUtils {

    public static Cell[][] createEmptyCellArray(int rows, int cols) {
        return new Cell[rows][cols];
    }

    public static Cell[][] createEmptyCellArray(int rows, int cols, Function<Position, Cell> creator) {
        final Cell[][] cells = new Cell[rows][cols];
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                cells[r][c] = creator.apply(new Position(r, c));
            }
        }

        return cells;
    }

    public static GameBoard createGameBoard(int rows, int cols, Function<Position, Cell> creator) {
        return new GameBoard(rows, cols, createEmptyCellArray(rows, cols, creator));
    }
}

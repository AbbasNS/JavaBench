package pa1.util;

public class GameStateSerializer {

    private GameStateSerializer() {
    }

    public static Path writeTo(final GameState gameState, final Path outputFile) throws FileAlreadyExistsException {
    }

    static void writeTo(final GameState gameState, final BufferedWriter writer) throws IOException {
    }

    public static GameState loadFrom(final Path inputFile) throws FileNotFoundException {
    }

    static GameState loadFrom(final BufferedReader reader) throws IOException {
    }

    private static char toCellChar(final Cell cell) {
    }

    private static Cell fromCellChar(final char c, final Position position) {
    }
}

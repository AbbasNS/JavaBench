package assignment.game;

public abstract class AbstractSokobanGame implements SokobanGame {

    protected final GameState state;

    protected AbstractSokobanGame(GameState gameState) {
    }

    protected boolean shouldStop() {
    }

    protected ActionResult processAction(Action action) {
    }
}

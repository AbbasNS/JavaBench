package assignment.tui;

import assignment.actions.Exit;
import assignment.actions.InvalidInput;
import assignment.game.GameState;
import assignment.game.Position;
import assignment.utils.TestKind;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.HashSet;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import static org.mockito.Mockito.*;

class TerminalSokobanGameTest {

    @Tag(TestKind.PUBLIC)
    @Test
    void testGameLoop() {
        final var gameState = mock(GameState.class);
        final var inputEngine = mock(TerminalInputEngine.class);
        final var renderingEngine = mock(TerminalRenderingEngine.class);
        when(gameState.isWin()).thenReturn(false);
        when(inputEngine.fetchAction())
            .thenReturn(new InvalidInput(0, ""))
            .thenReturn(new Exit(0));

        final var game = new TerminalSokobanGame(gameState, inputEngine, renderingEngine);
        game.run();

        final var inOrder = inOrder(inputEngine, renderingEngine);

        // Before loop
        inOrder.verify(renderingEngine).render(eq(gameState));

        // First round
        inOrder.verify(inputEngine).fetchAction();
        inOrder.verify(renderingEngine).render(eq(gameState));

        // Second round
        inOrder.verify(inputEngine).fetchAction();
        inOrder.verify(renderingEngine).render(eq(gameState));

        verify(gameState, atLeastOnce()).getUndoQuota();
        verify(gameState, atLeast(0)).isWin();
        verify(renderingEngine, atLeastOnce()).message(any());
    }

    @Tag(TestKind.PUBLIC)
    @Test
    void testTwoPlayers() {
        final var gameState = mock(GameState.class);
        final var inputEngine = mock(TerminalInputEngine.class);
        final var renderingEngine = mock(TerminalRenderingEngine.class);
        when(gameState.getAllPlayerPositions()).thenReturn(new HashSet<>(Arrays.asList(Position.of(1, 1), Position.of(1, 2))));

        assertDoesNotThrow(() -> new TerminalSokobanGame(gameState, inputEngine, renderingEngine));
    }
}

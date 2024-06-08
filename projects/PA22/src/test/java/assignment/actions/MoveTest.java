package assignment.actions;

import assignment.game.Position;
import assignment.utils.TestKind;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MoveTest {

    private final Position pos = Position.of(233, 233);

    @Tag(TestKind.PUBLIC)
    @Test
    void moveLeft() {
        assertEquals(
            Position.of(232, 233),
            new Move.Left(-1).nextPosition(pos)
        );
    }
}

package pa1.model;

import org.jetbrains.annotations.NotNull;

import java.util.Objects;

/**
 * A single cell on the game board.
 */
public abstract class Cell implements BoardElement {

    @NotNull
    private final Position position;

    /**
     * Creates an instance of {@link Cell} at the given position on the game board.
     *
     * @param position The position where this cell belongs at.
     */
    protected Cell(@NotNull final Position position) {
        this.position = Objects.requireNonNull(position);
    }

    /**
     * @return The {@link Position} of this cell on the game board.
     */
    @NotNull
    public final Position getPosition() {
        return this.position;
    }
}

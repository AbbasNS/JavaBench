package pa1.model;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

/**
 * A {@link Cell} on the game board which can contain an {@link Entity}.
 *
 * <p>
 * This class should observe and enforce the following constraints:
 * </p>
 * <ul>
 *     <li>There must be at most one entity owned by each cell; In other words, there should never be two entities'
 *     {@link Entity#getOwner()} pointing to the same {@link EntityCell}.</li>
 *     <li>There must be at most one cell owning each entity; In other words, there should never be two cells'
 *     {@link EntityCell#getEntity()} pointing to the same {@link Entity}.</li>
 * </ul>
 * <p>
 * More information is provided in the Javadoc of the methods in this class.
 * </p>
 */
public class EntityCell extends Cell {

    /**
     * The entity which resides on this cell.
     */
    @Nullable
    Entity entity = null;

    /**
     * Creates an instance of {@link EntityCell} at the given game board position.
     *
     * @param position The position where this cell belongs at.
     */
    public EntityCell(@NotNull final Position position) {
        this(position, null);
    }

    /**
     * Creates an instance of {@link EntityCell} at the given game board position.
     *
     * @param position      The position where this cell belongs at.
     * @param initialEntity The initial entity present in this cell.
     */
    public EntityCell(@NotNull final Position position, @Nullable final Entity initialEntity) {
        super(position);
        setEntity(initialEntity);
    }

    /**
     * Replaces the entity currently present in this cell.
     *
     * <p>
     * This method should perform <em>ownership transfer</em> on the new entity.
     * </p>
     * <p>
     * In other words, in addition to just setting {@link EntityCell#entity} of this instance, this method should also:
     * </p>
     * <ul>
     *     <li>Unset the {@link Entity#getOwner} of the previous entity owned by this instance, since we no longer own
     *     the entity.</li>
     *     <li>Unset the {@link EntityCell#entity} of the previous cell owning the {@code newEntity}, since the previous
     *     owner of the new entity no longer owns the entity.</li>
     *     <li>Set the {@link Entity#getOwner} of {@code newEntity} to this instance, since we now own the new entity.
     *     </li>
     * </ul>
     *
     * @param newEntity The new {@link Entity} to place in this cell.
     * @return The previous entity in this cell, or {@code null} if no entity is previously present in this cell.
     */
    @Nullable
    public Entity setEntity(@Nullable final Entity newEntity) {
        final var prevEntity = getEntity();

        // If we used to own an entity, we no longer do after this method returns; Reset the owner of the entity
        if (prevEntity != null) {
            prevEntity.setOwner(null);
        }

        // Perform ownership transfer if the new entity was originally bound to another cell
        if (newEntity != null && newEntity.getOwner() != null) {
            this.entity = newEntity.getOwner().setEntity(null);
        } else {
            this.entity = newEntity;
        }

        // Finally, set the owner of the new entity to us
        if (this.entity != null) {
            this.entity.setOwner(this);
        }

        return prevEntity;
    }

    /**
     * @return The entity currently present in this cell, or {@code null} if there is no entity present.
     */
    @Nullable
    public final Entity getEntity() {
        return entity;
    }

    @Override
    public char toUnicodeChar() {
        return getEntity() != null ? getEntity().toUnicodeChar() : '.';
    }

    @Override
    public char toASCIIChar() {
        return getEntity() != null ? getEntity().toASCIIChar() : '.';
    }
}

package pa1.model;

public abstract class Entity implements BoardElement {

    private EntityCell owner;

    protected Entity() {
    }

    protected Entity(final EntityCell owner) {
    }

    public final EntityCell setOwner(final EntityCell owner) {
    }

    public final EntityCell getOwner() {
    }
}

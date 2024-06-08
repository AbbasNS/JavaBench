package assignment.protocol;

public class Move implements Cloneable {

    private Place source;

    private Place destination;

    public Move(Place source, Place destination) {
    }

    public Move(int sourceX, int sourceY, int destinationX, int destinationY) {
    }

    public Move(Place source, int destinationX, int destinationY) {
    }

    /* Getters start */
    public Place getSource() {
    }

    public Place getDestination() {
    }

    /* Getters end */
    /* Object methods start */
    @Override
    public boolean equals(Object o) {
    }

    @Override
    public int hashCode() {
    }

    @Override
    public String toString() {
    }

    @Override
    public Move clone() throws CloneNotSupportedException {
    }
    /* Object methods end */
}

package assignment.actions;

public abstract class Move extends Action {

    protected Move(int initiator) {
    }

    public abstract Position nextPosition(Position currentPosition) {
    }

    public static final class Down extends Move {

        public Down(int initiator) {
        }

        @Override
        public Position nextPosition(Position currentPosition) {
        }
    }

    public static final class Left extends Move {

        public Left(int initiator) {
        }

        @Override
        public Position nextPosition(Position currentPosition) {
        }
    }

    public static final class Right extends Move {

        public Right(int initiator) {
        }

        @Override
        public Position nextPosition(Position currentPosition) {
        }
    }

    public static final class Up extends Move {

        public Up(int initiator) {
        }

        @Override
        public Position nextPosition(Position currentPosition) {
        }
    }
}

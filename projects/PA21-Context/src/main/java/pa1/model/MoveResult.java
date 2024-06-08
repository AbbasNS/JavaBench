package pa1.model;

public abstract class MoveResult {

    public final Position newPosition;

    public static class Valid extends MoveResult {

        public final Position origPosition;

        private Valid(final Position newPosition, final Position origPosition) {
        }

        public static final class Alive extends Valid {

            public final List<Position> collectedGems;

            public final List<Position> collectedExtraLives;

            public Alive(final Position newPosition, final Position origPosition) {
            }

            public Alive(final Position newPosition, final Position origPosition, final List<Position> collectedGems, final List<Position> collectedExtraLives) {
            }
        }

        public static final class Dead extends Valid {

            public final Position minePosition;

            public Dead(final Position newPosition, final Position minePosition) {
            }
        }
    }

    public static final class Invalid extends MoveResult {

        public Invalid(final Position newPosition) {
        }
    }

    private MoveResult(final Position newPosition) {
    }
}

package assignment.actions;

public abstract class ActionResult {

    protected final Action action;

    protected ActionResult(Action action) {
    }

    public Action getAction() {
    }

    public static final class Success extends ActionResult {

        public Success(Action action) {
        }
    }

    public static final class Failed extends ActionResult {

        private final String reason;

        public String getReason() {
        }

        public Failed(Action action, String reason) {
        }
    }
}

package assignment.game;

public class GameState {

    public GameState(GameMap map) {
    }

    public Position getPlayerPositionById(int id) {
    }

    public Set<Position> getAllPlayerPositions() {
    }

    public Entity getEntity(Position position) {
    }

    public Set<Position> getDestinations() {
    }

    public Optional<Integer> getUndoQuota() {
    }

    public boolean isWin() {
    }

    public void move(Position from, Position to) {
    }

    public void checkpoint() {
    }

    public void undo() {
    }

    public int getMapMaxWidth() {
    }

    public int getMapMaxHeight() {
    }
}

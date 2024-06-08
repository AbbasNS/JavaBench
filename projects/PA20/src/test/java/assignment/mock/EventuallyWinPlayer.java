package assignment.mock;

import assignment.protocol.Color;
import assignment.protocol.Game;
import assignment.protocol.Move;

public class EventuallyWinPlayer extends MockPlayer {
    public EventuallyWinPlayer(Color color) {
        super(color);
    }

    @Override
    public Move nextMove(Game game, Move[] availableMoves) {
        int minDistance = Integer.MAX_VALUE;
        Move best = availableMoves[0];
        for (Move move :
                availableMoves) {
            int dist = Math.abs(move.getDestination().x() - move.getSource().x()) +
                    Math.abs(move.getDestination().y() - move.getSource().y());
            if (dist <= minDistance) {
                minDistance = dist;
                best = move;
            }
        }
        return best;
    }
}

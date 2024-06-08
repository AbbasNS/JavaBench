package assignment;

import assignment.actions.Action;
import assignment.actions.ActionResult;
import assignment.actions.InvalidInput;
import assignment.game.GameState;
import assignment.game.InputEngine;
import assignment.game.RenderingEngine;

import static org.mockito.Mockito.mock;

/**
 * This class contains references to the public members that are not coverd by the test cases.
 * This is to make sure the declared public members are not changed with compilation.
 */
@SuppressWarnings("ALL")
public class SanityChecking {

    void referenceMembers() {
        Action a = null;
        int x = a.getInitiator();

        ActionResult ar = null;
        Action aa = ar.getAction();
        ActionResult.Failed f = null;
        String sss = f.getReason();

        InvalidInput i = null;
        String s = i.getMessage();

        InputEngine ie = null;
        Action aaa = ie.fetchAction();

        RenderingEngine re = null;
        re.message("");
        re.render(mock(GameState.class));
    }

}

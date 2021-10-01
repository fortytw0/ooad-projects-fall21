import java.util.Comparator;
import java.util.List;

public class HighestFirstStack extends Stack{
    public void doAction(Wares ware) {
        // reference https://stackoverflow.com/questions/33487063/java-8-sort-list-of-objects-by-attribute-without-custom-comparator
        List<Games> stack = ware.getGames();
        if(stack != null && !stack.isEmpty()) {
            stack.sort(Comparator.comparing(a -> a.getBoxHeight()));
            }
        }
    }


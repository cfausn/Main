/*
* PolyRoot.java
*
* Version:
* 1
*
* Revisions:
* 2/2/15 (submitted revision)
* */
package poly.stu;

import poly.stu.PolyEval;
import poly.stu.PolyDerive;
import static java.lang.Math.abs;

import java.util.ArrayList;

/**
 * Calculates the root of a given ArrayList of integers based on Newton's method.
 * @author Colin Fausnaught (cjf1613)
 */
public class PolyRoot {
    /**
     * Constant Values to implement newton's method.
     * */
    private static final double EPSILON = 0.0001;
    private static final double INITIAL_GUESS = 0.1;
    private static final int MAX_ITERATIONS = 100;

    /**
     * computeRoot implements the newtonsMethod function by taking an ArrayList to compute
     * and using the constant values mentioned above.
     *
     * @param   poly        An ArrayList of Integers
     * @return              An ArrayList returned from the recursive newtonsMethod function
     * */
    public static double computeRoot(ArrayList<Integer> poly){
        return newtonsMethod(poly,INITIAL_GUESS,0);

    }

    /**
     * newtonsMethod is a recursive function which uses a method specified by Newton.
     *
     * @param   poly        An ArrayList of Integers
     * @param   x0          A double variable that changes as the function recurses
     * @param   iter        An Integer variable that keeps track of the number of recursions
     * @return              A Double; the calculated root
     * */
    private static double newtonsMethod(ArrayList<Integer> poly,
                                        double x0,
                                        int iter){
        if(iter > MAX_ITERATIONS || abs(PolyEval.evaluate(poly,x0)) <= EPSILON) return x0;
        else {
            return newtonsMethod(poly, (x0 - ((PolyEval.evaluate(poly, x0)) / PolyEval.evaluate(PolyDerive.computeDerivative(poly), x0))), iter + 1);
        }
    }
} //Class PolyRoot

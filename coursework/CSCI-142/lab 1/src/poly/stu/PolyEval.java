/*
* PolyEval.java
*
* Version:
* 1
*
* Revisions:
* 2/2/15 (submitted revision)
* */

package poly.stu;

import java.util.ArrayList;
import static java.lang.Math.pow; //used to get the power

/**
 * Evaluates a polynomial given a value for x.
 * @author Colin Fausnaught (cjf1613)
 */
public class PolyEval {
    /**
     * evaluate will evaluate a polynomial given a value for x and a polynomial.
     *
     * @param   poly        An ArrayList which contains the integers for a Polynomial
     * @param   x           A value for x to evaluate.
     * @return  sum         Double, the value of the polynomial at x
     * */
    public static double evaluate(ArrayList<Integer> poly, double x){
        double sum = 0.0; //returned later
        if(poly.size() == 1) return poly.get(0); //if polynomial has only a constant (no x value), return it
        else{
            if(isZero(poly) == false) {
                for (int i = 0; i < poly.size(); i++)
                    if (i == 0) sum += (double) poly.get(i);
                    else sum = sum + ((pow(x, i)) * poly.get(i));
            }
            else return 0.0; //just in case polynomial is empty
        }
        return sum;

    }

    /**
     * isZero checks if the polynomial contains all zeros or not
     *
     * @param   poly           An ArrayList of integers to check for all zeros
     * @return  zero OR false  Boolean, returns zero (true) if true or simply false if false.
     * */
    public static boolean isZero(ArrayList<Integer> poly){
        boolean zero = false;
        for(Integer element : poly){
            if(element == 0) zero = true;

            else return false;
        }
        return zero;
    }
} //class PolyEval


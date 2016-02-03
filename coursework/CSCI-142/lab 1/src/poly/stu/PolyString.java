/*
* PolyString.java
*
* Version:
* 1
*
* Revisions:
* 2/2/15 (submitted revision)
* */

package poly.stu;

import java.util.ArrayList;

/**
 * This class can return a string representation of a polynomial of order n, 
 * in the form:
 * <p>
 * <pre>
 * x^n + x^n-1 + ... x^1 + constant
 * </pre>
 * </p>
 *
 * @author sps (Sean Strout @ RIT CS)
 * @author Colin Fausnaught (cjf1613)
 */
public class PolyString {
    /**
     * The displayed variable name
     */
    private final static String VARIABLE_NAME = "x";

    /**
     * Get the string representation of the polynomial.  For example:
     * <p>
     * <pre>
     * poly=[1] -> "1"
     * poly=[3, -1] -> "-x + 3"
     * poly=[0, 3] -> "3x + 0"
     * poly=[2, -1, -2, 1] -> "x^3 + -2x^2 + -x + 1"
     * poly=[-5, 0, 0, 3, 3, 1] -> "x^5 + 3x^4 + 3x^3 + -5"
     * </pre>
     * </p>
     * 
     * @param poly A list representing the polynomial, in reverse order.
     * @pre poly is not an empty list.  Minimally it will contain
     *      a constant term.
     * @return A string representation of the polynomial.
     */
    public static String getString(ArrayList<Integer> poly) {
        String result = "";
        
        // step backwards through list from highest to lowest order term
        for (int exp=poly.size()-1; exp>=0; --exp) {
            int coeff = poly.get(exp);
            // include constant term, but don't want 1x or -1x
            if (exp == 0 || Math.abs(coeff) > 1) {  
                result += coeff;
            }
            // include non-constant, non-zero terms
            if (exp > 0 && coeff != 0) { 
                if (coeff == -1) { 
                    result += "-"; // ... + -x ...
                }
                result += VARIABLE_NAME; 
                if (exp > 1) {    // don't want x^1          
                    result += "^" + exp;
                } 
                result += " + ";  // ok because constant always shows at end 
            }
        }
        
        return result;
    }
}

/*
* PolyMain.java
*
* Version:
* 1
*
* Revisions:
* Colin Fausnaught, 2/2/15
* */

import poly.stu.PolyRoot;
import poly.stu.PolyString;
import poly.stu.PolyEval;

import poly.stu.PolyDerive;


import java.util.ArrayList;
import java.util.Scanner;

/**
 * A class that works with polynomials that are provided on the command line,
 * in reverse order.  If the polynomial is empty, it will display a usage 
 * message and exit:
 * <p>
 * <pre>
 * $ java Poly
 * Usage: java Poly term0...
 * </pre>
 * </p>
 * 
 * <p>
 * Otherwise, various operations described in the main method are performed
 * using the polynomial.  Five example runs are provided: 
 * </p>
 * 
 * <p>
 * <pre>
 * Example 1: java PolyMain 1
 * f(x) = 1
 * Enter x: 0.0
 * f(0.0) = 1.0
 * f'(x) = 0
 * Root: none exist
 * 
 * Example 2: java PolyMain 3 -1
 * f(x) = -x + 3
 * Enter x: 4.5
 * f(4.5) = -1.5
 * f'(x) = -1
 * Root: 3.0
 * 
 * Example 3: java PolyMain 0 3
 * f(x) = 3x + 0
 * Enter x: -2.0
 * f(-2.0) = -6.0
 * f'(x) = 3
 * Root: -1.3877787807814457E-17
 * 
 * Example 4: java PolyMain 2 -1 -2 1
 * f(x) = x^3 + -2x^2 + -x + 2
 * Enter x: 2.0
 * f(2.0) = 0.0
 * f'(x) = 3x^2 + -4x + -1
 * Root: 2.0000000358875707
 * 
 * Example 5: java PolyMain -5 0 0 3 3 1
 * f(x) = x^5 + 3x^4 + 3x^3 + -5
 * Enter x: -3.9
 * f(-3.9) = -391.16669
 * f'(x) = 5x^4 + 12x^3 + 9x^2 + 0
 * Root: 0.9128992721006024
 * </pre>
 * </p>
 * 
 * @author sps (Sean Strout @ RIT CS)
 */
public class PolyMain {    
    /**
     * The main method:
     * <p>
     * <pre>
     * 1. reads the polynomial from the command line and displays it.
     * 2. prompts the user for a value of x.
     * 3. evaluates the polynomial with the supplied value of x and
     * displays the result of the evaluation.
     * 4. compute/display the derivative of the polynomial.
     * 5. compute/display the root of the polynomial, using Newton's method,
     * if one exists.
     * </pre>
     * </p>
     * 
     * @param args The polynomial, in reverse order of terms, whose
     *  coefficients are integers.
     */
    public static void main(String[] args) {
        // check for one or more command line arguments
        if (args.length == 0) { 
            System.out.println("Usage: java Poly term0 ...");
            return;
        }
        System.out.println("wat");
        // read the polynomial in from the command line
        ArrayList<Integer> poly = new ArrayList<Integer>();
        for (String val : args) {
            poly.add(Integer.parseInt(val));
        }
        
        // pretty print the polynomial
        System.out.println("f(x) = " + PolyString.getString(poly));

        
        // get a value for x and evaluate the polynomial with it
        Scanner in = new Scanner(System.in);
        System.out.print("Enter x: ");
        double x = in.nextDouble();
        System.out.println("f(" + x + ") = " + PolyEval.evaluate(poly, x));
        in.close();

        // get the derivative of the polynomial and pretty print it
        ArrayList<Integer> deriv = PolyDerive.computeDerivative(poly);
        System.out.println("f'(x) = " + PolyString.getString(deriv));

        // get the root of the polynomial, if derivative is not 0
        if (PolyEval.isZero(deriv)) {
            System.out.println("Root: none exist");
        } else {
            System.out.println("Root: " + PolyRoot.computeRoot(poly));
        }


    }
}
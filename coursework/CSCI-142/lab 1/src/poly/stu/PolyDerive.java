/*
* PolyDerive.java
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
 * Finds the derivative of an ArrayList of Integers.
 *
 * @author Colin Fausnaught (cjf1613)
 */
public class PolyDerive {


    /**
     * computeDerivative computes a derivative based on a passed list.
     * @param   poly        ArrayList of Integers to derive
     * @return  newList     ArrayList of Integers that have been derived from poly
     * */
    public static ArrayList<Integer> computeDerivative(ArrayList<Integer> poly){
        ArrayList<Integer> newList = new ArrayList<Integer>(); //derived list
        if (poly.size() == 0){
            newList.add(0);
            return newList; //Just in case an empty ArrayList is passed
        }
        else{
            for(int i = 1; i < poly.size(); i++) newList.add(poly.get(i) * i);
            return newList;
        }

    }
}
